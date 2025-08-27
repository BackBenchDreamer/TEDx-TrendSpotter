from .base_agent import BaseAgent
from ..embeddings.embedding_manager import EmbeddingManager
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class IdeaValidationAgent(BaseAgent):
    def __init__(self):
        super().__init__("IdeaValidationAgent")
        self.embedding_manager = EmbeddingManager()
        
    def process(self, query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Validate if an idea has been covered"""
        self.log_action("Processing idea validation", query)
        
        # Search for similar ideas
        results = self.embedding_manager.search_similar(query, n_results=10)
        
        if not results['documents'][0]:
            return {
                "validation_status": "UNIQUE",
                "similarity_score": 0.0,
                "message": "Your idea appears to be unique! No similar talks found."
            }
        
        # Calculate similarity scores
        similarity_analysis = self.analyze_similarity(query, results)
        validation_status = self.determine_status(similarity_analysis)
        
        return {
            "validation_status": validation_status["status"],
            "similarity_score": similarity_analysis["max_similarity"],
            "similar_talks": similarity_analysis["similar_talks"],
            "recommendations": validation_status["recommendations"],
            "message": validation_status["message"]
        }
    
    def analyze_similarity(self, query, results):
        """Analyze similarity between query and existing talks"""
        # Get query embedding
        query_embedding = self.embedding_manager.embedding_model.encode([query])
        
        similarities = []
        similar_talks = []
        
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
            # Get document embedding
            doc_embedding = self.embedding_manager.embedding_model.encode([doc])
            
            # Calculate similarity
            similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]
            similarities.append(similarity)
            
            if similarity > 0.7:  # High similarity threshold
                similar_talks.append({
                    "title": metadata.get('title', 'Unknown'),
                    "speaker": metadata.get('speaker', 'Unknown'),
                    "similarity": float(similarity),
                    "snippet": doc[:150] + "..."
                })
        
        return {
            "similarities": similarities,
            "max_similarity": max(similarities) if similarities else 0.0,
            "similar_talks": sorted(similar_talks, key=lambda x: x['similarity'], reverse=True)
        }
    
    def determine_status(self, similarity_analysis):
        """Determine validation status based on similarity"""
        max_sim = similarity_analysis["max_similarity"]
        
        if max_sim > 0.85:
            return {
                "status": "HIGHLY_SIMILAR",
                "message": "Your idea is very similar to existing talks. Consider a different angle.",
                "recommendations": [
                    "Find a unique perspective or application",
                    "Focus on recent developments or personal experience",
                    "Combine with other concepts for originality"
                ]
            }
        elif max_sim > 0.7:
            return {
                "status": "SIMILAR",
                "message": "Similar ideas exist, but there may be room for a fresh perspective.",
                "recommendations": [
                    "Identify what's unique about your approach",
                    "Focus on underexplored aspects",
                    "Consider audience-specific angles"
                ]
            }
        elif max_sim > 0.5:
            return {
                "status": "SOMEWHAT_COVERED",
                "message": "Some related content exists, but your idea has potential for originality.",
                "recommendations": [
                    "Your idea has good potential",
                    "Consider how to differentiate from existing talks",
                    "Focus on your unique insights or experience"
                ]
            }
        else:
            return {
                "status": "UNIQUE",
                "message": "Your idea appears to be quite unique! Great potential for a TEDx talk.",
                "recommendations": [
                    "Excellent! Your idea seems original",
                    "Focus on clear storytelling and practical applications",
                    "Consider the broader impact of your idea"
                ]
            }
