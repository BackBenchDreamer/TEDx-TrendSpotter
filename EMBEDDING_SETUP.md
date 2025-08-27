# Embedding System Setup Guide

This guide covers the setup and initialization of the TEDx TrendSpotter embedding system for Retrieval-Augmented Generation (RAG).

## 🏗️ System Architecture

The embedding system consists of several key components:

### Core Components
- **EmbeddingManager**: Handles vector embeddings creation and similarity search
- **ChromaDB**: Local vector database for storing embeddings  
- **SentenceTransformers**: Creates semantic embeddings from text
- **TEDxDataProcessor**: Processes and chunks TEDx transcript data

### Setup Scripts
- `setup.py`: Complete automated setup process
- `verify_setup.py`: Validates system configuration
- `scripts/setup_local_models.py`: Downloads and caches ML models
- `scripts/initialize_database.py`: Initializes the embedding database

## 🚀 Quick Setup

### Automated Setup (Recommended)
```bash
# Run the complete setup process
python setup.py
```

### Manual Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup environment
cp .env.example .env

# 3. Create directories and download models
python scripts/setup_local_models.py

# 4. Verify setup
python verify_setup.py
```

## 📁 Directory Structure

After setup, your project should have:

```
TEDx-TrendSpotter/
├── src/
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedding_manager.py    # Core embedding functionality
│   └── utils/
│       ├── __init__.py
│       └── data_processor.py       # Text processing utilities
├── scripts/
│   ├── setup_local_models.py       # Model download script
│   ├── initialize_database.py      # Database setup script
│   └── data_collection.py          # Data collection script
├── data/
│   ├── embeddings/                 # ChromaDB storage
│   ├── processed/                  # Processed transcript data
│   └── raw/                        # Raw transcript data
├── streamlit_app/
│   └── app.py                      # Web interface
├── requirements.txt                # Dependencies
├── .env.example                    # Environment configuration
├── setup.py                       # Automated setup script
└── verify_setup.py                # Setup verification
```

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Database Configuration
CHROMADB_PATH=./data/embeddings/chroma_db
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=microsoft/DialoGPT-medium

# Data Processing
TEDX_DATA_PATH=./data/processed/tedx_talks.csv
MAX_DOCUMENTS=1000
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

### Model Configuration
- **Embedding Model**: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- **Vector Database**: ChromaDB (local, persistent storage)
- **Text Generation**: DialoGPT-medium (for conversation features)

## 🔄 Initialization Workflow

### 1. Model Setup
```bash
python scripts/setup_local_models.py
```
- Downloads SentenceTransformers embedding model
- Downloads text generation model
- Creates necessary directories

### 2. Data Collection
```bash
python scripts/data_collection.py
```
- Scrapes TEDx talk metadata
- Downloads transcripts
- Saves raw data to `data/raw/`

### 3. Data Processing
The data processor automatically:
- Cleans transcript text
- Extracts key topics
- Chunks text for RAG
- Saves processed data to `data/processed/`

### 4. Database Initialization
```bash
python scripts/initialize_database.py
```
- Creates embeddings for all text chunks
- Stores embeddings in ChromaDB
- Builds search index
- Performs system validation test

## 🧪 Testing and Validation

### Verify Setup
```bash
python verify_setup.py
```
Checks:
- ✅ Python version compatibility
- ✅ File structure completeness
- ✅ Python syntax validation
- ✅ Dependencies specification
- ✅ Environment configuration

### Test Embedding System
```bash
python test_embedding_setup.py
```
Tests:
- ✅ Module imports
- ✅ EmbeddingManager functionality
- ✅ Data processing pipeline
- ✅ Search and retrieval

## 🚀 Launch Application

After successful setup:
```bash
streamlit run streamlit_app/app.py
```

## 🛠️ Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure dependencies are installed
pip install -r requirements.txt

# Check Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Memory Issues**
- Reduce batch size in `embedding_manager.py`
- Process data in smaller chunks
- Use CPU-only mode for models

**Network Issues**
- Check internet connection for model downloads
- Configure proxy if needed
- Use cached models if available

### Manual Dependency Installation
If automated installation fails:
```bash
# Core ML dependencies
pip install torch torchvision torchaudio
pip install transformers sentence-transformers
pip install chromadb

# Data processing
pip install pandas numpy scikit-learn
pip install nltk

# Web interface
pip install streamlit plotly

# Utilities
pip install python-dotenv tqdm beautifulsoup4
```

## 📊 System Requirements

### Minimum Requirements
- **Python**: 3.8+
- **RAM**: 4GB+ (8GB recommended)
- **Storage**: 2GB+ for models and data
- **Internet**: Required for initial setup

### Recommended Setup
- **Python**: 3.10+
- **RAM**: 8GB+
- **GPU**: Optional (CUDA-compatible for faster processing)
- **Storage**: 5GB+ for larger datasets

## 🔍 System Validation

A properly setup system should:
1. ✅ Import all core modules without errors
2. ✅ Initialize EmbeddingManager successfully
3. ✅ Create embeddings for sample text
4. ✅ Perform similarity search
5. ✅ Return relevant results

## 📚 Next Steps

After setup completion:
1. **Data Collection**: Gather TEDx transcript data
2. **Database Population**: Create embeddings for your dataset
3. **Application Launch**: Start the Streamlit interface
4. **Custom Configuration**: Adjust models and parameters as needed

For detailed usage instructions, see the main [README.md](README.md).