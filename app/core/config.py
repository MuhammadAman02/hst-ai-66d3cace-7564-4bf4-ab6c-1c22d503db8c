"""Application configuration using Pydantic Settings v2"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Application settings
    app_name: str = Field(default="AI Engineer Portfolio", description="Application name")
    debug: bool = Field(default=False, description="Debug mode")
    version: str = Field(default="1.0.0", description="Application version")
    
    # Server settings
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8080, description="Server port")
    
    # Security settings
    secret_key: str = Field(
        default="your-secret-key-change-in-production",
        description="Secret key for JWT tokens"
    )
    access_token_expire_minutes: int = Field(
        default=30,
        description="Access token expiration time in minutes"
    )
    
    # File paths
    static_dir: str = Field(default="app/static", description="Static files directory")
    upload_dir: str = Field(default="app/static/uploads", description="Upload directory")
    resume_path: str = Field(default="app/static/files", description="Resume files directory")
    resume_filename: str = Field(default="AI_Engineer_Resume.txt", description="Resume filename")
    
    # Email settings (optional - for contact form)
    smtp_server: str = Field(default="", description="SMTP server for email")
    smtp_port: int = Field(default=587, description="SMTP port")
    smtp_username: str = Field(default="", description="SMTP username")
    smtp_password: str = Field(default="", description="SMTP password")
    contact_email: str = Field(
        default="contact@ai-engineer.dev",
        description="Contact email address"
    )
    
    # External API settings
    unsplash_access_key: str = Field(
        default="",
        description="Unsplash API access key for professional images"
    )
    
    # Database settings (if needed for future enhancements)
    database_url: str = Field(
        default="sqlite:///./portfolio.db",
        description="Database URL"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create global settings instance
settings = Settings()

# Ensure required directories exist
Path(settings.static_dir).mkdir(parents=True, exist_ok=True)
Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
Path(settings.resume_path).mkdir(parents=True, exist_ok=True)