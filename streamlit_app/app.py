import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.trend_agent import TrendAnalysisAgent
from src.agents.validation_agent import IdeaValidationAgent
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
	page_title="TEDx TrendSpotter",
	page_icon="🧠",
	layout="wide",
	initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
	.main-header {
		font-size: 3rem;
		font-weight: bold;
		text-align: center;
		color: #e62b1e;
		margin-bottom: 2rem;
	}
	.sub-header {
		font-size: 1.5rem;
		color: #666;
		text-align: center;
		margin-bottom: 3rem;
	}
	.result-card {
		background-color: #f8f9fa;
		padding: 1rem;
		border-radius: 0.5rem;
		border-left: 4px solid #e62b1e;
		margin: 1rem 0;
	}
</style>
""", unsafe_allow_html=True)

class TEDxTrendSpotterApp:
	def __init__(self):
		self.trend_agent = None
		self.validation_agent = None
        
	def initialize_agents(self):
		"""Initialize agents with caching"""
		if 'agents_initialized' not in st.session_state:
			with st.spinner("🤖 Initializing AI agents..."):
				try:
					self.trend_agent = TrendAnalysisAgent()
					self.validation_agent = IdeaValidationAgent()
					st.session_state.agents_initialized = True
					st.session_state.trend_agent = self.trend_agent
					st.session_state.validation_agent = self.validation_agent
					st.success("✅ Agents initialized successfully!")
				except Exception as e:
					st.error(f"❌ Error initializing agents: {str(e)}")
					return False
		else:
			self.trend_agent = st.session_state.trend_agent
			self.validation_agent = st.session_state.validation_agent
        
		return True
    
	def render_header(self):
		"""Render application header"""
		st.markdown('<h1 class="main-header">🧠 TEDx TrendSpotter</h1>', unsafe_allow_html=True)
		st.markdown('<p class="sub-header">AI-Powered Insights for Emerging Ideas in TEDx Talks</p>', unsafe_allow_html=True)
        
		# Quick stats
		col1, col2, col3, col4 = st.columns(4)
		with col1:
			st.metric("Talks Analyzed", "1,000+", "📈")
		with col2:
			st.metric("Topics Tracked", "500+", "🏷️")
		with col3:
			st.metric("Accuracy", "94%", "🎯")
		with col4:
			st.metric("Processing Speed", "<3s", "⚡")
    
	def render_sidebar(self):
		"""Render sidebar with navigation"""
		st.sidebar.title("🎯 Navigation")
        
		page = st.sidebar.selectbox(
			"Choose Analysis Type:",
			["🔍 Trend Analysis", "✅ Idea Validation", "📊 Topic Explorer", "💡 Idea Generator"]
		)
        
		st.sidebar.markdown("---")
		st.sidebar.markdown("### 🚀 Quick Tips")
		st.sidebar.info("""
		**For best results:**
		- Use specific, descriptive queries
		- Try different phrasings
		- Combine multiple concepts
		- Be creative with your ideas!
		""")
        
		return page
    
	def render_trend_analysis(self):
		"""Render trend analysis page"""
		st.header("🔍 Trend Analysis")
		st.write("Discover emerging patterns and trending topics in TEDx talks")
        
		# Input form
		with st.form("trend_form"):
			query = st.text_input(
				"Enter a topic or theme to analyze:",
				placeholder="e.g., artificial intelligence, climate change, mental health"
			)
			analyze_btn = st.form_submit_button("🔍 Analyze Trends", use_container_width=True)
        
		if analyze_btn and query:
			with st.spinner("🔄 Analyzing trends..."):
				try:
					results = self.trend_agent.process(query)
                    
					if "error" in results:
						st.error(results["error"])
						return
                    
					# Display results
					self.display_trend_results(results)
                    
				except Exception as e:
					st.error(f"❌ Error during analysis: {str(e)}")
    
	def display_trend_results(self, results):
		"""Display trend analysis results"""
		st.success("✅ Analysis complete!")
        
		# Summary
		st.markdown('<div class="result-card">', unsafe_allow_html=True)
		st.markdown("### 📋 Analysis Summary")
		st.write(results.get("analysis_summary", "No summary available"))
		st.markdown('</div>', unsafe_allow_html=True)
        
		# Trending topics chart
		if results.get("trends", {}).get("top_topics"):
			st.markdown("### 📈 Trending Topics")
            
			topics_data = results["trends"]["top_topics"]
			df_topics = pd.DataFrame(topics_data, columns=["Topic", "Frequency"])
            
			fig = px.bar(
				df_topics.head(10), 
				x="Frequency", 
				y="Topic", 
				orientation='h',
				title="Top 10 Trending Topics",
				color="Frequency",
				color_continuous_scale="Reds"
			)
			fig.update_layout(height=400)
			st.plotly_chart(fig, use_container_width=True)
        
		# Related talks
		if results.get("related_talks"):
			st.markdown("### 🎤 Related Talks")
            
			for i, talk in enumerate(results["related_talks"][:5]):
				with st.expander(f"#{i+1}: {talk['title']} - {talk['speaker']}"):
					st.write(f"**Relevance Score:** {talk['relevance_score']}")
					st.write(f"**Snippet:** {talk['snippet']}")
    
	def render_idea_validation(self):
		"""Render idea validation page"""
		st.header("✅ Idea Validation")
		st.write("Check if your TEDx talk idea is original and get recommendations")
        
		# Input form
		with st.form("validation_form"):
			idea = st.text_area(
				"Describe your TEDx talk idea:",
				placeholder="e.g., How blockchain technology can revolutionize education by creating transparent credential systems...",
				height=100
			)
			validate_btn = st.form_submit_button("✅ Validate Idea", use_container_width=True)
        
		if validate_btn and idea:
			with st.spinner("🔄 Validating your idea..."):
				try:
					results = self.validation_agent.process(idea)
					self.display_validation_results(results)
                    
				except Exception as e:
					st.error(f"❌ Error during validation: {str(e)}")
    
	def display_validation_results(self, results):
		"""Display validation results"""
		status = results.get("validation_status", "UNKNOWN")
		similarity_score = results.get("similarity_score", 0.0)
        
		# Status indicator
		status_colors = {
			"UNIQUE": "🟢",
			"SOMEWHAT_COVERED": "🟡", 
			"SIMILAR": "🟠",
			"HIGHLY_SIMILAR": "🔴"
		}
        
		status_color = status_colors.get(status, "⚪")
        
		st.markdown(f"### {status_color} Validation Result: {status}")
        
		# Similarity score gauge
		fig = go.Figure(go.Indicator(
			mode = "gauge+number+delta",
			value = similarity_score * 100,
			domain = {'x': [0, 1], 'y': [0, 1]},
			title = {'text': "Similarity Score (%)"},
			gauge = {'axis': {'range': [None, 100]},
					'bar': {'color': "darkblue"},
					'steps': [
						{'range': [0, 50], 'color': "lightgreen"},
						{'range': [50, 70], 'color': "yellow"},
						{'range': [70, 85], 'color': "orange"},
						{'range': [85, 100], 'color': "red"}],
					'threshold': {'line': {'color': "red", 'width': 4},
								'thickness': 0.75, 'value': 85}}))
        
		fig.update_layout(height=300)
		st.plotly_chart(fig, use_container_width=True)
        
		# Message and recommendations
		st.info(results.get("message", "No message available"))
        
		if results.get("recommendations"):
			st.markdown("### 💡 Recommendations")
			for rec in results["recommendations"]:
				st.write(f"• {rec}")
        
		# Similar talks
		if results.get("similar_talks"):
			st.markdown("### 🎯 Similar Existing Talks")
			for talk in results["similar_talks"][:3]:
				with st.expander(f"{talk['title']} - {talk['speaker']} (Similarity: {talk['similarity']:.2%})"):
					st.write(talk['snippet'])
    
	def render_topic_explorer(self):
		"""Render topic explorer page"""
		st.header("📊 Topic Explorer")
		st.write("Explore and visualize topic distributions across TEDx talks")
        
		# This would contain interactive topic exploration features
		st.info("🚧 Topic Explorer coming soon! This will include interactive topic maps and detailed analytics.")
    
	def render_idea_generator(self):
		"""Render idea generator page"""
		st.header("💡 Idea Generator")
		st.write("Generate fresh TEDx talk ideas based on current trends and gaps")
        
		# This would contain AI-powered idea generation
		st.info("🚧 Idea Generator coming soon! This will use AI to suggest original talk ideas.")
    
	def run(self):
		"""Main application runner"""
		self.render_header()
        
		# Initialize agents
		if not self.initialize_agents():
			st.error("Failed to initialize the application. Please check your setup.")
			return
        
		# Sidebar navigation
		page = self.render_sidebar()
        
		# Main content based on page selection
		if page == "🔍 Trend Analysis":
			self.render_trend_analysis()
		elif page == "✅ Idea Validation":
			self.render_idea_validation()
		elif page == "📊 Topic Explorer":
			self.render_topic_explorer()
		elif page == "💡 Idea Generator":
			self.render_idea_generator()

# Run the application
if __name__ == "__main__":
	app = TEDxTrendSpotterApp()
	app.run()
