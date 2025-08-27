import streamlit as st
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Configure page
st.set_page_config(
    page_title="TEDx TrendSpotter",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🎯 TEDx TrendSpotter")
st.subtitle("AI-Powered Insights for Emerging Ideas in TEDx Talks")

# Sidebar
st.sidebar.header("🚀 System Status")

# Check if embedding system is ready
try:
    from src.embeddings.embedding_manager import EmbeddingManager
    from src.utils.data_processor import TEDxDataProcessor
    
    st.sidebar.success("✅ Core modules loaded")
    system_ready = True
except ImportError as e:
    st.sidebar.error(f"❌ Import error: {e}")
    st.sidebar.warning("Please install dependencies: pip install -r requirements.txt")
    system_ready = False

# Main content
if system_ready:
    st.success("🎉 Embedding system is properly configured!")
    
    # Feature overview
    st.header("🔍 Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💡 Idea Gap Analysis
        - Identify unexplored topics
        - Find research opportunities
        - Discover innovation spaces
        
        ### 🔍 Concept Validation
        - Check if your idea has been covered
        - Find similar talks and themes
        - Analyze topic saturation
        """)
    
    with col2:
        st.markdown("""
        ### 📈 Trend Forecasting
        - Discover emerging themes
        - Track topic evolution
        - Predict future directions
        
        ### 🧠 Speaker Intelligence
        - Analyze speaking patterns
        - Identify successful themes
        - Compare presentation styles
        """)
    
    # System setup guide
    st.header("🛠️ Setup Guide")
    
    with st.expander("Setup Instructions", expanded=False):
        st.markdown("""
        **1. Install Dependencies**
        ```bash
        pip install -r requirements.txt
        ```
        
        **2. Setup Environment**
        ```bash
        cp .env.example .env
        # Edit .env with your configurations
        ```
        
        **3. Download Models**
        ```bash
        python scripts/setup_local_models.py
        ```
        
        **4. Collect Data**
        ```bash
        python scripts/data_collection.py
        ```
        
        **5. Initialize Database**
        ```bash
        python scripts/initialize_database.py
        ```
        """)
    
    # Demo section (placeholder)
    st.header("🎬 Demo")
    st.info("Once the system is fully initialized, you'll be able to:")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.text_input("🔎 Search for similar talks", placeholder="Enter your topic or idea...")
        st.slider("Number of results", min_value=1, max_value=20, value=5)
    
    with demo_col2:
        st.selectbox("Search mode", ["Semantic similarity", "Keyword search", "Topic clusters"])
        st.checkbox("Include speaker analysis")
    
    if st.button("🚀 Search (Demo)"):
        st.warning("Please complete the setup steps above to enable full functionality.")

else:
    st.error("🚫 System not ready")
    
    st.markdown("""
    ### 📋 Setup Required
    
    The embedding system needs to be properly configured before use. Please follow these steps:
    
    1. **Install Dependencies**
       ```bash
       pip install -r requirements.txt
       ```
    
    2. **Verify Setup**
       ```bash
       python verify_setup.py
       ```
    
    3. **Complete Setup Process**
       Follow the setup guide in the expanded section above.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🔬 Built with open-source tools • 💰 Zero-cost architecture • 🌍 Accessible AI for everyone</p>
</div>
""", unsafe_allow_html=True)
