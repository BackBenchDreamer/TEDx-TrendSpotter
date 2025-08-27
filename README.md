# TEDx TrendSpotter
*AI-Powered Insights for Emerging Ideas in TEDx Talks*

**Uncover innovation patterns** | **Validate unique topics** | **Built with Open Source & Free APIs**

***

## Description

TEDx TrendSpotter is an intelligent Retrieval-Augmented Generation (RAG) platform that analyzes thousands of TEDx talk transcripts to help aspiring speakers, researchers, and innovators discover untapped ideas and identify emerging trends. Built entirely with open-source tools and free API tiers, this platform makes AI-powered innovation insights accessible to everyone.

Whether you're preparing for your first TEDx talk, conducting academic research, or seeking the next breakthrough innovation, TrendSpotter eliminates the guesswork by providing data-driven intelligence about what topics have been explored, what gaps remain, and where the conversation is heading next - all without breaking the bank.

***

## Key Features

✓ **Idea Gap Analysis** - Identify unexplored topics using free Hugging Face models  
✓ **Concept Validation** - Check if your idea has been covered using local vector search  
✓ **Trend Forecasting** - Discover emerging themes with open-source NLP tools  
✓ **Speaker Intelligence** - Analyze patterns using free sentiment analysis APIs  
✓ **Innovation Mapping** - Visualize connections with NetworkX and Matplotlib  
✓ **Local Processing** - Run entirely offline after initial setup  
✓ **Memory-Enhanced Conversations** - Context-aware responses with local storage

***

## Quick Start

Get TrendSpotter running in 3 simple steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/TEDx-TrendSpotter-RAG.git
cd TEDx-TrendSpotter-RAG

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

***

## Installation

### Requirements
- **Python 3.8+**
- **4GB+ RAM** (for local model inference)
- **2GB+ Storage** (for embeddings and models)

### Budget-Friendly Setup

1. **Clone and navigate to project directory:**
```bash
git clone https://github.com/yourusername/TEDx-TrendSpotter-RAG.git
cd TEDx-TrendSpotter-RAG
```

2. **Create virtual environment:**
```bash
python -m venv tedx_env
source tedx_env/bin/activate  # On Windows: tedx_env\Scripts\activate
```

3. **Install free dependencies:**
```bash
pip install transformers sentence-transformers chromadb langchain-community 
pip install streamlit pandas numpy matplotlib networkx plotly beautifulsoup4
pip install huggingface-hub datasets scikit-learn wordcloud seaborn
```

4. **Optional: Set up free API limits (if desired):**
```bash
cp .env.example .env
# Add free tier API keys (optional):
# HUGGINGFACE_API_KEY=your_free_hf_key (for faster inference)
# SERPAPI_KEY=your_free_serpapi_key (100 searches/month)
```

5. **Download and initialize local models:**
```bash
python scripts/setup_local_models.py
```

6. **Launch application:**
```bash
streamlit run app.py
```

***

## Dependency Versions (as installed)

The following versions are installed in the virtual environment:

- transformers==4.55.4
- sentence-transformers==2.2.2
- torch==2.8.0
- torchaudio==2.8.0
- torchvision==0.23.0
- langchain==0.0.335
- langchain-community==0.0.38
- pandas==2.3.2
- numpy==1.26.4
- scikit-learn==1.7.1
- datasets==2.14.6
- requests==2.31.0
- beautifulsoup4==4.12.2
- youtube-transcript-api==0.6.1
- serpapi==0.1.5
- streamlit==1.28.1
- plotly==5.17.0
- networkx==3.5
- tqdm==4.67.1
- pyyaml==6.0.2

### Not Installed (please install manually if needed):
- chromadb
- matplotlib
- seaborn
- wordcloud
- python-dotenv

If you require any of the above, install them using pip:

```bash
pip install chromadb matplotlib seaborn wordcloud python-dotenv
```

***

## Budget-Friendly Architecture

**Zero-Cost Core Components:**

- **Local Embeddings**: SentenceTransformers (all-MiniLM-L6-v2) - completely free
- **Vector Database**: ChromaDB - open source, runs locally
- **Language Model**: Hugging Face Transformers (Llama-2-7B-Chat via free tier)
- **Web Scraping**: BeautifulSoup + Requests for TEDx transcript collection
- **Analysis Engine**: scikit-learn for clustering and trend analysis

**Optional Free Tier APIs:**
- **Hugging Face Inference API**: 1,000 requests/month free
- **SerpAPI**: 100 searches/month free (for real-time validation)

***

## Cost Breakdown

| Component | Cost | Alternative |
|-----------|------|-------------|
| Vector Storage | **FREE** (ChromaDB local) | Pinecone ($70+/month) |
| Embeddings | **FREE** (Local models) | OpenAI ($0.0001/token) |
| Language Model | **FREE** (HF free tier) | GPT-4 ($0.03/1K tokens) |
| Web Search | **FREE** (100/month) | Tavily ($50+/month) |
| **Total Monthly** | **$0** | **$120+** |

***

## Free Data Sources

✓ **TEDx YouTube Transcripts** - Public API, no cost  
✓ **Internet Archive TEDx Collection** - Open access  
✓ **Wikipedia TEDx Speaker Pages** - Free scraping  
✓ **Reddit TEDx Communities** - Public discussions  
✓ **Academic Papers on TEDx** - ArXiv and open journals

***

## Performance Optimization

**Local Processing Tips:**
- Use GPU acceleration if available (`pip install torch torchvision`)
- Cache embeddings locally to avoid recomputation
- Batch process documents for efficiency
- Use lightweight models for real-time inference

**Memory Management:**
- Process documents in chunks to avoid RAM overflow
- Use memory mapping for large datasets
- Implement lazy loading for model inference

***

## Contributing

We welcome contributions, especially budget-conscious improvements! Priority areas:

1. **Model Optimization** - Make inference faster on CPU-only systems
2. **Data Collection** - Add more free TEDx transcript sources
3. **UI Improvements** - Enhance Streamlit interface
4. **Documentation** - Help others replicate the setup

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

***

## Free Hosting Options

Deploy your TrendSpotter instance for free:

- **Streamlit Community Cloud** - Free hosting for Streamlit apps
- **Hugging Face Spaces** - Free GPU-enabled hosting
- **Google Colab** - Run notebooks with free GPU access
- **Railway/Render** - Free tiers for containerized apps

***

## Use Cases

**For Students:**
- Research paper topic discovery without expensive tools
- Academic project development on zero budget
- Learning AI/ML concepts with practical application

**For Entrepreneurs:**
- Market research without consultant fees
- Innovation scouting using free resources
- Idea validation before investment

**For Educators:**
- Classroom demonstrations of AI concepts
- Student project templates
- Research methodology teaching

***

## Technical Stack

- **Framework**: LangChain Community (free components)
- **Vector Database**: ChromaDB (open source)
- **Embeddings**: SentenceTransformers (free local models)
- **Language Model**: Hugging Face Transformers (free tier)
- **Frontend**: Streamlit (open source)
- **Data Processing**: Pandas, NumPy (open source)
- **Visualization**: Matplotlib, Plotly (open source)

***

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

***

## Budget-Conscious Acknowledgments

This project proves that cutting-edge AI research doesn't require expensive infrastructure. Built entirely with open-source tools and community resources, making innovation insights accessible to everyone regardless of budget constraints.

**GitHub Topics**: `tedx` `open-source-ai` `free-apis` `sentence-transformers` `chromadb` `budget-friendly` `local-llm` `huggingface` `streamlit` `zero-cost`
