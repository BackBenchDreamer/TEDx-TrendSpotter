from sentence_transformers import SentenceTransformer
import chromadb
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
from dotenv import load_dotenv

load_dotenv()

class EmbeddingManager:
    def __init__(self):
        self.model_name = os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
        self.db_path = os.getenv('CHROMADB_PATH', './data/embeddings/chroma_db')
        # Initialize sentence transformer
        print(f"🤖 Loading embedding model: {self.model_name}")
        self.embedding_model = SentenceTransformer(self.model_name)
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = None
    def create_collection(self, collection_name="tedx_talks"):
        """Create or get ChromaDB collection"""
        try:
            self.collection = self.client.get_collection(collection_name)
            print(f"📚 Loaded existing collection: {collection_name}")
        except:
            self.collection = self.client.create_collection(collection_name)
            print(f"🆕 Created new collection: {collection_name}")
        return self.collection
    def embed_documents(self, chunks_file):
        """Create embeddings for all document chunks"""
        print("🔮 Creating embeddings for document chunks...")
        # Load chunks
        chunks_df = pd.read_csv(chunks_file)
        # Create collection
        self.create_collection()
        # Process in batches for memory efficiency
        batch_size = 100
        total_batches = len(chunks_df) // batch_size + 1
        for i in tqdm(range(0, len(chunks_df), batch_size), desc="Embedding batches"):
            batch_df = chunks_df.iloc[i:i+batch_size]
            # Prepare batch data
            texts = batch_df['chunk_text'].tolist()
            embeddings = self.embedding_model.encode(texts)
            # Prepare metadata
            metadatas = []
            ids = []
            for idx, row in batch_df.iterrows():
                metadata = {
                    'talk_id': str(row['talk_id']),
                    'chunk_id': str(row['chunk_id']),
                    'title': row['title'],
                    'speaker': row['speaker'],
                    'key_topics': str(row['key_topics'])
                }
                metadatas.append(metadata)
                ids.append(f"talk_{row['talk_id']}_chunk_{row['chunk_id']}")
            # Add to collection
            self.collection.add(
                embeddings=embeddings.tolist(),
                documents=texts,
                metadatas=metadatas,
                ids=ids
            )
        print(f"✅ Created embeddings for {len(chunks_df)} chunks")
    def search_similar(self, query, n_results=5):
        """Search for similar documents"""
        if not self.collection:
            self.create_collection()
        # Create query embedding
        query_embedding = self.embedding_model.encode([query])
        # Search
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results
        )
        return results
    def get_collection_stats(self):
        """Get statistics about the collection"""
        if not self.collection:
            self.create_collection()
        count = self.collection.count()
        return {"total_chunks": count}

# Usage
if __name__ == "__main__":
    manager = EmbeddingManager()
    manager.embed_documents('./data/processed/tedx_talks_processed_chunks.csv')
    # Test search
    results = manager.search_similar("artificial intelligence and future")
    print("🔍 Sample search results:")
    for i, doc in enumerate(results['documents'][0]):
        print(f"{i+1}. {doc[:100]}...")
