#!/usr/bin/env python3
"""
Test script to validate embedding system setup
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import pandas as pd
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        from sentence_transformers import SentenceTransformer
        print("✅ sentence-transformers imported successfully")
    except ImportError as e:
        print(f"❌ sentence-transformers import failed: {e}")
        return False
    
    try:
        import chromadb
        print("✅ chromadb imported successfully")
    except ImportError as e:
        print(f"❌ chromadb import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    return True

def test_embedding_manager():
    """Test EmbeddingManager class"""
    print("\n🤖 Testing EmbeddingManager...")
    
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from src.embeddings.embedding_manager import EmbeddingManager
        print("✅ EmbeddingManager imported successfully")
        
        # Test initialization (this will try to load the model)
        manager = EmbeddingManager()
        print("✅ EmbeddingManager initialized successfully")
        
        return True
    except Exception as e:
        print(f"❌ EmbeddingManager test failed: {e}")
        return False

def test_data_processor():
    """Test TEDxDataProcessor class"""
    print("\n📊 Testing TEDxDataProcessor...")
    
    try:
        from src.utils.data_processor import TEDxDataProcessor
        print("✅ TEDxDataProcessor imported successfully")
        
        processor = TEDxDataProcessor()
        print("✅ TEDxDataProcessor initialized successfully")
        
        # Test text processing
        test_text = "This is a test transcript with some um filler words and... extra punctuation!"
        cleaned = processor.clean_transcript(test_text)
        print(f"✅ Text cleaning test passed: '{cleaned}'")
        
        return True
    except Exception as e:
        print(f"❌ TEDxDataProcessor test failed: {e}")
        return False

def test_directories():
    """Test if necessary directories exist or can be created"""
    print("\n📁 Testing directory structure...")
    
    directories = [
        './data/embeddings',
        './data/processed', 
        './data/raw'
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Directory created/verified: {directory}")
        except Exception as e:
            print(f"❌ Failed to create directory {directory}: {e}")
            return False
    
    return True

def main():
    """Run all tests"""
    print("🚀 Starting Embedding System Setup Tests\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("Directory Tests", test_directories), 
        ("Data Processor Tests", test_data_processor),
        ("Embedding Manager Tests", test_embedding_manager),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print('='*50)
        
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("📋 Test Summary")
    print('='*50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Embedding system is ready.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please install missing dependencies:")
        print("   pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())