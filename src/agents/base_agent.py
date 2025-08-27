from abc import ABC, abstractmethod
from typing import List, Dict, Any
import logging

class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        
    @abstractmethod
    def process(self, query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process a query and return results"""
        pass
    
    def log_action(self, action: str, details: str = ""):
        """Log agent actions"""
        self.logger.info(f"{self.name}: {action} - {details}")
