#!/usr/bin/env python3
"""
Installation and setup verification script for TEDx TrendSpotter
This script checks the setup without requiring all dependencies to be installed.
"""

import sys
import os
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible. Need Python 3.8+")
        return False


def check_file_structure():
    """Check if all required files and directories exist"""
    print("\n📁 Checking file structure...")
    
    required_files = [
        'requirements.txt',
        'src/__init__.py',
        'src/embeddings/__init__.py',
        'src/embeddings/embedding_manager.py',
        'src/utils/__init__.py',
        'src/utils/data_processor.py',
        'scripts/setup_local_models.py',
        'scripts/initialize_database.py',
        'scripts/data_collection.py',
        'streamlit_app/app.py',
        '.env.example'
    ]
    
    required_dirs = [
        'data/embeddings',
        'data/processed',
        'data/raw'
    ]
    
    all_good = True
    
    # Check files
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            all_good = False
    
    # Check directories
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✅ {dir_path}/")
        else:
            print(f"❌ Missing directory: {dir_path}/")
            all_good = False
    
    return all_good


def check_syntax():
    """Check Python syntax of all main files"""
    print("\n🔍 Checking Python syntax...")
    
    python_files = [
        'src/embeddings/embedding_manager.py',
        'src/utils/data_processor.py',
        'scripts/setup_local_models.py',
        'scripts/initialize_database.py',
        'scripts/data_collection.py'
    ]
    
    all_good = True
    
    for file_path in python_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    compile(f.read(), file_path, 'exec')
                print(f"✅ {file_path} - syntax OK")
            except SyntaxError as e:
                print(f"❌ {file_path} - syntax error: {e}")
                all_good = False
        else:
            print(f"⚠️  {file_path} - file not found")
    
    return all_good


def check_requirements():
    """Analyze requirements.txt"""
    print("\n📦 Checking requirements.txt...")
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return False
    
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    
    required_packages = [
        'transformers',
        'sentence-transformers', 
        'torch',
        'chromadb',
        'langchain',
        'pandas',
        'numpy',
        'streamlit',
        'python-dotenv',
        'beautifulsoup4',
        'youtube-transcript-api'
    ]
    
    all_good = True
    for package in required_packages:
        if package in requirements:
            print(f"✅ {package} specified in requirements")
        else:
            print(f"❌ {package} missing from requirements")
            all_good = False
    
    return all_good


def check_environment_setup():
    """Check environment configuration"""
    print("\n🔧 Checking environment setup...")
    
    if os.path.exists('.env.example'):
        print("✅ .env.example exists")
        
        with open('.env.example', 'r') as f:
            env_content = f.read()
        
        required_vars = [
            'CHROMADB_PATH',
            'EMBEDDING_MODEL',
            'LLM_MODEL'
        ]
        
        all_good = True
        for var in required_vars:
            if var in env_content:
                print(f"✅ {var} configured in .env.example")
            else:
                print(f"❌ {var} missing from .env.example")
                all_good = False
        
        return all_good
    else:
        print("❌ .env.example not found")
        return False


def suggest_next_steps():
    """Suggest next steps for setup"""
    print("\n🚀 Next Steps for Setup:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Copy .env.example to .env and configure as needed")
    print("3. Run setup script: python scripts/setup_local_models.py")
    print("4. Collect data: python scripts/data_collection.py")
    print("5. Initialize database: python scripts/initialize_database.py")
    print("6. Launch app: streamlit run streamlit_app/app.py")


def main():
    """Run all checks"""
    print("🏗️  TEDx TrendSpotter - Embedding System Setup Verification")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("File Structure", check_file_structure),
        ("Python Syntax", check_syntax),
        ("Requirements", check_requirements),
        ("Environment Setup", check_environment_setup)
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n{'='*40}")
        print(f"Running: {check_name}")
        print('='*40)
        
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ {check_name} failed with exception: {e}")
            results.append((check_name, False))
    
    # Summary
    print(f"\n{'='*60}")
    print("📋 Setup Verification Summary")
    print('='*60)
    
    all_passed = True
    for check_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{check_name}: {status}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All checks passed! Embedding system structure is ready.")
        print("You can now install dependencies and start using the system.")
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
    
    suggest_next_steps()
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())