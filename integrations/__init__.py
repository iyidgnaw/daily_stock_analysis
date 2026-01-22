# -*- coding: utf-8 -*-
"""
Integration modules

This package contains third-party service integrations:
- feishu_doc: Feishu document management
"""

from .feishu_doc import FeishuDocManager

__all__ = [
    'FeishuDocManager',
]
