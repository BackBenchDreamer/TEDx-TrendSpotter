"""
Data processing utilities for TEDx TrendSpotter.

This module provides classes and functions for processing TEDx transcript data,
cleaning text, extracting topics, and chunking documents for the RAG system.
"""

from .data_processor import TEDxDataProcessor

__all__ = ['TEDxDataProcessor']