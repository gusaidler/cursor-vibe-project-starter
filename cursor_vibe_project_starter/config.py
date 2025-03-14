"""
Configuration module for Cursor Vibe Project Starter.

This module handles configuration settings using Pydantic.
"""

import os
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    
    openrouter_api_key: str
    openrouter_model: str
    openrouter_api_url: str
    
    class Config:
        """Pydantic config."""
        
        env_file = ".env"
        env_prefix = "" 