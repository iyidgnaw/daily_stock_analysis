# -*- coding: utf-8 -*-
"""
Core analysis modules

This package contains the core analysis logic:
- analyzer: AI-powered stock analysis using Gemini
- stock_analyzer: Technical trend analysis
- market_analyzer: Market overview and review
"""

from core.analyzer import GeminiAnalyzer, AnalysisResult, STOCK_NAME_MAP
from core.stock_analyzer import StockTrendAnalyzer, TrendAnalysisResult
from core.market_analyzer import MarketAnalyzer
from core.storage import get_db, DatabaseManager
from core.config import get_config, Config

__all__ = [
    'GeminiAnalyzer',
    'AnalysisResult',
    'STOCK_NAME_MAP',
    'StockTrendAnalyzer',
    'TrendAnalysisResult',
    'MarketAnalyzer',
    'get_db',
    'DatabaseManager',
    'get_config',
    'Config',
]
