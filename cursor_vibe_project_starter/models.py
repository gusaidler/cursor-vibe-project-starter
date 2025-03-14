"""
Data models for Cursor Vibe Project Starter.

This module contains the data models used throughout the application.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class AppType(str, Enum):
    """Enum for application types."""
    
    WEB = "web"
    MOBILE = "mobile"
    CLI = "cli"
    GAME = "game"
    DESKTOP = "desktop"
    API = "api"
    OTHER = "other"


class AppProject(BaseModel):
    """Model representing an app project."""
    
    name: str
    idea: str
    app_type: AppType
    tech_stack_preference: Optional[str] = None
    key_features: List[str] = []
    target_audience: Optional[str] = None 