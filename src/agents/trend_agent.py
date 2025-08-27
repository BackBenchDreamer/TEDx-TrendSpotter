from .base_agent import BaseAgent
from ..embeddings.embedding_manager import EmbeddingManager
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class TrendAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("TrendAnalysisAgent")
        self.embedding_manager = EmbeddingManager()
        
    def process(self, query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze trends related to the query"""
        self.log_action("Processing trend analysis", query)
        
        # Search for relevant talks
        results = self.embedding_manager.search_similar(query, n_results=20)
        
        if not results['documents'][0]:
            return {"error": "No relevant talks found"}
        
        # Extract topics and patterns
        trends = self.extract_trends(results)
        gaps = self.identify_gaps(results, query)
        
        return {
            "trends": trends,
            "gaps": gaps,
            "related_talks": self.format_talks(results),
            "analysis_summary": self.generate_summary(trends, gaps)
        }
    
    def extract_trends(self, results):
        """Extract trending topics from search results"""
        all_topics = []
        
        for metadata in results['metadatas'][0]:
            topics = eval(metadata.get('key_topics', '[]'))
            all_topics.extend(topics)
        
        # Count topic frequency
        topic_counts = Counter(all_topics)
        trending = topic_counts.most_common(10)
        
        return {
            "top_topics": trending,
            "total_topics": len(set(all_topics)),
            "topic_distribution": dict(trending)
        }
    
    def identify_gaps(self, results, query):
        """Identify potential gaps in coverage"""
        covered_aspects = set()
        
        for doc in results['documents'][0]:
            # Simple keyword extraction for gap analysis
            words = doc.lower().split()
            covered_aspects.update(words)
        
        # This is simplified - in a real system you'd use more sophisticated NLP
        query_aspects = set(query.lower().split())
        potential_gaps = query_aspects - covered_aspects
        
        return {
            "covered_aspects": len(covered_aspects),
            "potential_gaps": list(potential_gaps),
            "coverage_score": len(covered_aspects) / (len(covered_aspects) + len(potential_gaps))
        }
    
    def format_talks(self, results):
        """Format talk information for display"""
        talks = []
        
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
            talks.append({
                "title": metadata.get('title', 'Unknown'),
                "speaker": metadata.get('speaker', 'Unknown'),
                "snippet": doc[:200] + "...",
                "relevance_score": i + 1
            })
        
        return talks
    
    def generate_summary(self, trends, gaps):
        """Generate analysis summary"""
        summary = f"""
        Trend Analysis Summary:
        - Found {len(trends['top_topics'])} trending topics
        - Coverage score: {gaps['coverage_score']:.2f}
        - Top trend: {trends['top_topics'][0][0] if trends['top_topics'] else 'None'}
        """
        return summary.strip()
