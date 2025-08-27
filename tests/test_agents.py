import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.trend_agent import TrendAnalysisAgent
from src.agents.validation_agent import IdeaValidationAgent

class TestTrendAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TrendAnalysisAgent()
    
    def test_process_query(self):
        """Test basic query processing"""
        result = self.agent.process("artificial intelligence")
        self.assertIn("trends", result)
        self.assertIn("gaps", result)
    
    def test_empty_query(self):
        """Test handling of empty queries"""
        result = self.agent.process("")
        # Should handle gracefully
        self.assertIsInstance(result, dict)

class TestValidationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = IdeaValidationAgent()
    
    def test_idea_validation(self):
        """Test idea validation"""
        result = self.agent.process("revolutionary new idea about space exploration")
        self.assertIn("validation_status", result)
        self.assertIn("similarity_score", result)

if __name__ == "__main__":
    unittest.main()
