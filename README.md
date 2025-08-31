# TEDx-TrendSpotter (Agentic RAG with LangChain-Groq)

***

## Project Overview

TEDx-TrendSpotter is an advanced Retrieval-Augmented Generation (RAG) system featuring an **agentic AI workflow** built exclusively with LangChain's integration with Groq. This project harnesses cutting-edge language modeling powered by the **openai/gpt-oss-20b** model via Groq, delivering high intelligence, rapid response times, and cost-efficient inference at scale. It is designed to provide dynamic, context-aware information retrieval and generation, ideal for extracting insights from large datasets like TEDx talk transcripts using a flexible agent-based approach.

***

## Key Features

- **Agent-based RAG:** Combines retrieval with intelligent agent reasoning to dynamically process and respond using multiple tools and document stores.
- **Groq Integration:** Utilizes LangChain's Groq integration for efficient LLM operations powered by the openai/gpt-oss-20b model.
- **Speed and Efficiency:** Provides fast inference with low latency and reduced cost, supporting real-time, context-aware AI applications.
- **Multi-Namespace Vector Stores:** Supports parallel multi-tenancy and segmented data access through namespaced Pinecone-like vector storage.
- **Conversational Memory:** Maintains contextual chat history to enable coherent multi-turn interactions.
- **Tokenization and Chunking:** Employs sophisticated text splitting and embedding techniques to optimize data ingestion and retrieval.

***

## Technologies Used

- **langchain-groq:** LangChain's Groq provider for accelerated inference.
- **LangChain:** Framework for building composable AI applications and RAG pipelines.
- **Groq:** High-performance inference engine powering the openai/gpt-oss-20b model.
- **OpenAI Embeddings:** Transformer-based embeddings for semantic search.
- **Pinecone Vector Store:** For scalable and efficient vector similarity search.
- **Tiktoken:** Tokenizer compatible with GPT-style models.
- **Python:** Main programming language with deep ecosystem support.

***

## Getting Started

### Prerequisites

- Python 3.8+
- Groq API key (obtainable from the Groq platform)
- Required Python packages (install via `pip`)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/BackBenchDreamer/TEDx-TrendSpotter.git
   cd TEDx-TrendSpotter
   ```

2. **Set up and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file or set environment variables directly to include your Groq API key:

   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```

   Or on Windows PowerShell:

   ```powershell
   setx GROQ_API_KEY "your_groq_api_key_here"
   ```

***

## Usage

### Running the Agentic RAG System

Start the RAG pipeline and agent:

```python
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.vectorstores import PineconeVectorStore

# Initialize Groq LLM with gpt-oss-20b
llm = ChatGroq(
    groq_api_key="your_groq_api_key",
    model_name="openai/gpt-oss-20b",
    temperature=0.0,
    max_tokens=512
)

# Set up vector store retriever (example with Pinecone)
vectorstore = PineconeVectorStore(
    index_name="tedx-trendspotter",
    namespace="main",
    embedding=OpenAIEmbeddings()
)

# Create RetrievalQA chain with memory and agentic reasoning
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Example query
question = "What are the emerging trends in TEDx talks on climate change?"
answer = qa_chain.run(question)
print(answer)
```

Alternatively, run the full agent executor for interactive multi-tool querying.

***

## Why Groq?

Groq enables the deployment of the **openai/gpt-oss-20b** model — a compact Mixture-of-Experts (MoE) language model optimized for **high intelligence**, **cost efficiency**, and **rapid response**. Compared to traditional models, gpt-oss-20b offers similar reasoning capabilities to proprietary OpenAI models but with:

- **Lower inference costs** suited for budget-conscious applications.
- **Fast token generation speeds** allowing real-time interaction.
- **Memory-efficient deployment** on consumer-grade hardware.
- **Built-in function and tool use support** for advanced agentic workflows.

This makes Groq and the gpt-oss-20b model an ideal foundation for a dynamic agentic RAG system that balances performance, affordability, and scalability.

***

This project exemplifies how to build intelligent, efficient, and agent-powered retrieval systems leveraging the state-of-the-art Groq platform and LangChain ecosystem to unlock actionable insights from large unstructured data collections like TEDx talk transcripts.
