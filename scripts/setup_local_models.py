from sentence_transformers import SentenceTransformer
from transformers import pipeline
import os

def download_embedding_model():
	"""Download and cache embedding model"""
	print("📥 Downloading embedding model...")
	model = SentenceTransformer('all-MiniLM-L6-v2')
	print("✅ Embedding model ready!")
	return model

def download_text_generation_model():
	"""Download and cache text generation model"""
	print("📥 Downloading text generation model...")
	generator = pipeline('text-generation', 
						model='microsoft/DialoGPT-medium',
						tokenizer='microsoft/DialoGPT-medium')
	print("✅ Text generation model ready!")
	return generator

def setup_directories():
	"""Create necessary directories"""
	directories = [
		'./data/embeddings',
		'./data/processed',
		'./data/raw'
	]
    
	for directory in directories:
		os.makedirs(directory, exist_ok=True)
		print(f"📁 Created directory: {directory}")

if __name__ == "__main__":
	print("🚀 Setting up local models...")
    
	setup_directories()
	embedding_model = download_embedding_model()
	text_model = download_text_generation_model()
    
	print("🎉 All models downloaded and ready!")
