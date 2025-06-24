"""Advanced professional visual asset management system with project-specific categories"""

import hashlib
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
import requests
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class ImageAsset:
    """Represents a professional image asset with fallback options"""
    primary_url: str
    fallback_url: str
    alt_text: str
    category: str
    width: int = 1200
    height: int = 800


class ProfessionalAssetManager:
    """Advanced professional visual asset management system"""
    
    # AI Engineer specific image categories
    AI_ENGINEER_CATEGORIES = {
        "hero": [
            "artificial intelligence", "machine learning", "data science",
            "technology", "coding", "computer science", "innovation"
        ],
        "professional": [
            "professional", "workspace", "office", "technology",
            "developer", "engineer", "modern office", "computer setup"
        ],
        "projects": [
            "data visualization", "neural networks", "algorithms",
            "computer vision", "robotics", "automation", "analytics",
            "deep learning", "ai research", "machine learning models"
        ],
        "skills": [
            "programming", "python", "tensorflow", "pytorch",
            "data analysis", "statistics", "mathematics", "algorithms"
        ],
        "team": [
            "teamwork", "collaboration", "tech team", "developers",
            "meeting", "brainstorming", "agile", "startup"
        ],
        "innovation": [
            "innovation", "future technology", "ai", "research",
            "breakthrough", "cutting edge", "digital transformation"
        ]
    }
    
    def __init__(self, cache_dir: Optional[Path] = None):
        """Initialize the asset manager with optional caching"""
        self.cache_dir = cache_dir or Path("app/static/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def get_ai_engineer_assets(self, sections_count: int = 6) -> Dict[str, List[ImageAsset]]:
        """Get contextually relevant professional images for AI engineer portfolio"""
        
        assets = {}
        
        for section, keywords in self.AI_ENGINEER_CATEGORIES.items():
            section_assets = []
            
            for i in range(min(sections_count, len(keywords))):
                keyword = keywords[i % len(keywords)]
                asset = self._create_image_asset(keyword, section, i)
                section_assets.append(asset)
            
            assets[section] = section_assets
        
        return assets
    
    def _create_image_asset(self, keyword: str, section: str, index: int) -> ImageAsset:
        """Create an image asset with multiple fallback options"""
        
        # Generate consistent seed for reproducible images
        seed = abs(hash(f"{keyword}_{section}_{index}")) % 10000
        
        # Primary source: Unsplash with specific keyword
        primary_url = f"https://source.unsplash.com/1200x800/?{keyword.replace(' ', '+')}&sig={seed}"
        
        # Fallback source: Lorem Picsum with seed
        fallback_url = f"https://picsum.photos/1200/800?random={seed}"
        
        # Generate descriptive alt text
        alt_text = f"Professional {keyword} imagery for {section} section"
        
        return ImageAsset(
            primary_url=primary_url,
            fallback_url=fallback_url,
            alt_text=alt_text,
            category=section,
            width=1200,
            height=800
        )
    
    def get_optimized_image_url(self, asset: ImageAsset, width: int = None, height: int = None) -> str:
        """Get optimized image URL for specific dimensions"""
        
        if width and height:
            # Try to get optimized version from Unsplash
            if "unsplash" in asset.primary_url:
                base_url = asset.primary_url.split('?')[0]
                params = asset.primary_url.split('?')[1] if '?' in asset.primary_url else ""
                return f"{base_url.replace('1200x800', f'{width}x{height}')}?{params}"
            
            # Fallback to Picsum with custom dimensions
            seed = abs(hash(asset.primary_url)) % 10000
            return f"https://picsum.photos/{width}/{height}?random={seed}"
        
        return asset.primary_url
    
    def validate_image_url(self, url: str) -> bool:
        """Validate if an image URL is accessible"""
        
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.warning(f"Image validation failed for {url}: {e}")
            return False
    
    def get_placeholder_image(self, width: int = 1200, height: int = 800, text: str = "Portfolio") -> str:
        """Get a placeholder image with custom text"""
        
        # Use a reliable placeholder service
        return f"https://via.placeholder.com/{width}x{height}/667eea/ffffff?text={text.replace(' ', '+')}"
    
    @staticmethod
    def generate_image_css() -> str:
        """Generate CSS for professional image handling with modern styling"""
        
        return """
        /* Professional Image System with Modern Styling */
        .hero-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .hero-image:hover {
            transform: translateY(-5px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.15);
        }
        
        .project-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 15px;
            transition: all 0.3s ease;
        }
        
        .project-image:hover {
            transform: scale(1.05);
        }
        
        .professional-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 15px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }
        
        .skills-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 12px;
            opacity: 0.8;
            transition: opacity 0.3s ease;
        }
        
        .skills-image:hover {
            opacity: 1;
        }
        
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        
        .image-card {
            position: relative;
            overflow: hidden;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            background: white;
        }
        
        .image-card:hover {
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            transform: translateY(-8px);
        }
        
        .image-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                to bottom, 
                transparent 0%, 
                rgba(102, 126, 234, 0.8) 100%
            );
            display: flex;
            align-items: flex-end;
            padding: 1.5rem;
            color: white;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .image-card:hover .image-overlay {
            opacity: 1;
        }
        
        .image-loading {
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: loading 1.5s infinite;
        }
        
        @keyframes loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
        
        .image-error {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 500;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-image {
                height: 300px;
                border-radius: 15px;
            }
            
            .professional-image {
                height: 250px;
            }
            
            .gallery-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }
            
            .image-card {
                border-radius: 15px;
            }
        }
        
        @media (max-width: 480px) {
            .hero-image {
                height: 250px;
                border-radius: 12px;
            }
            
            .project-image,
            .professional-image {
                height: 200px;
            }
        }
        """
    
    def get_section_specific_assets(self, section: str, count: int = 3) -> List[ImageAsset]:
        """Get assets for a specific portfolio section"""
        
        if section not in self.AI_ENGINEER_CATEGORIES:
            section = "professional"  # Default fallback
        
        keywords = self.AI_ENGINEER_CATEGORIES[section]
        assets = []
        
        for i in range(min(count, len(keywords))):
            keyword = keywords[i]
            asset = self._create_image_asset(keyword, section, i)
            assets.append(asset)
        
        return assets