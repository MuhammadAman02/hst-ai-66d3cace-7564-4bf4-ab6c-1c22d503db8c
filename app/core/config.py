"""Configuration settings for the AI Engineer Portfolio application"""

import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Application Info
    app_name: str = "AI Engineer Portfolio"
    app_version: str = "1.0.0"
    app_description: str = "Professional portfolio for AI Engineer showcasing ML/DL projects and expertise"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8080
    debug: bool = True
    
    # Contact Configuration
    contact_email: str = "contact@ai-engineer.dev"
    smtp_server: Optional[str] = None
    smtp_port: int = 587
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None
    
    # Social Media Links
    linkedin_url: str = "https://linkedin.com/in/ai-engineer"
    github_url: str = "https://github.com/ai-engineer"
    medium_url: str = "https://medium.com/@ai-engineer"
    twitter_url: str = "https://twitter.com/ai_engineer"
    
    # Resume Configuration
    resume_filename: str = "AI_Engineer_Resume.pdf"
    resume_path: str = "app/static/documents/"
    
    # Image Configuration
    default_image_quality: int = 85
    max_image_size: int = 1920
    image_cache_duration: int = 3600  # 1 hour
    
    # Analytics (optional)
    google_analytics_id: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()