"""Core package for the AI Engineer Portfolio application"""

from .config import settings
from .logger import app_logger
from .assets import ProfessionalAssetManager

__all__ = ["settings", "app_logger", "ProfessionalAssetManager"]