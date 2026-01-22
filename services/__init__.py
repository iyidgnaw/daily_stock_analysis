# -*- coding: utf-8 -*-
"""
Service modules

This package contains service layer modules:
- notification: Multi-channel notification service
- search_service: News and information search service
"""

from .notification import NotificationService, NotificationChannel, send_daily_report
from .search_service import SearchService, SearchResponse

__all__ = [
    'NotificationService',
    'NotificationChannel',
    'send_daily_report',
    'SearchService',
    'SearchResponse',
]
