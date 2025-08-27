import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.embeddings.embedding_manager import EmbeddingManager
from src.utils.data_processor import TEDxDataProcessor

def initialize_system():
	"""Initialize the complete system"""
	print("🏗️ Initializing TEDx TrendSpotter system...")
    
	# Check if processed data exists
	processed_file = './data/processed/tedx_talks_processed.csv'
	chunks_file = './data/processed/tedx_talks_processed_chunks.csv'
    
	if not os.path.exists(chunks_file):
		print("⚠️ Processed data not found. Please run data collection first.")
		print("Run: python scripts/data_collection.py")
		return False
    
	# Initialize embedding manager
	embedding_manager = EmbeddingManager()
    
	# Create embeddings
	embedding_manager.embed_documents(chunks_file)
    
	# Test the system
	test_query = "innovation in technology"
	results = embedding_manager.search_similar(test_query)
    
	print(f"🧪 Test query: '{test_query}'")
	print(f"✅ Found {len(results['documents'][0])} relevant chunks")
    
	stats = embedding_manager.get_collection_stats()
	print(f"📊 Database stats: {stats}")
    
	print("🎉 System initialization complete!")
	return True

if __name__ == "__main__":
	success = initialize_system()
	if success:
		print("\n🚀 Ready to run: streamlit run streamlit_app/app.py")
	else:
		print("\n❌ Initialization failed. Please check the steps above.")
