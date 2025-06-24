"""Advanced professional visual asset management system for AI Engineer portfolio"""

import hashlib
import requests
from typing import Dict, List, Optional
from urllib.parse import quote
import logging

logger = logging.getLogger(__name__)


class ProfessionalAssetManager:
    """Advanced professional visual asset management system with AI/tech focus"""
    
    AI_ENGINEER_CATEGORIES = {
        "hero": [
            "artificial intelligence", "machine learning", "data science", 
            "neural networks", "technology", "coding"
        ],
        "professional": [
            "professional", "workspace", "coding", "developer", 
            "technology", "computer science"
        ],
        "projects": [
            "data visualization", "artificial intelligence", "machine learning",
            "computer vision", "neural networks", "algorithms", "robotics",
            "deep learning", "data analysis", "technology innovation"
        ],
        "skills": [
            "brain", "network", "algorithm", "data", "analytics", 
            "artificial intelligence", "machine learning", "technology"
        ],
        "experience": [
            "teamwork", "collaboration", "office", "technology", 
            "professional", "business", "innovation"
        ],
        "contact": [
            "communication", "network", "professional", "connection",
            "technology", "collaboration"
        ]
    }
    
    FALLBACK_IMAGES = {
        "hero": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1200&h=800&fit=crop",
        "professional": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=300&fit=crop",
        "projects": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=350&h=200&fit=crop",
        "skills": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=300&h=200&fit=crop",
        "experience": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=250&fit=crop",
        "contact": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=300&fit=crop"
    }
    
    def __init__(self):
        self.cache = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AI-Engineer-Portfolio/1.0 (Professional Portfolio Application)'
        })
    
    def get_ai_engineer_assets(self, sections: Optional[List[str]] = None) -> Dict[str, List[Dict[str, str]]]:
        """Fetch contextually relevant professional images for AI engineer portfolio"""
        
        if sections is None:
            sections = list(self.AI_ENGINEER_CATEGORIES.keys())
        
        assets = {}
        
        for section in sections:
            if section not in self.AI_ENGINEER_CATEGORIES:
                continue
                
            section_images = []
            keywords = self.AI_ENGINEER_CATEGORIES[section]
            
            # Generate multiple images per section
            images_per_section = 3 if section == 'projects' else 2
            
            for i in range(images_per_section):
                keyword = keywords[i % len(keywords)]
                seed = self._generate_seed(f"ai_engineer_{section}_{i}")
                
                # Create multiple image sources for reliability
                primary_url = self._build_unsplash_url(keyword, 1200, 800, seed)
                secondary_url = self._build_picsum_url(1200, 800, seed)
                fallback_url = self.FALLBACK_IMAGES.get(section, self.FALLBACK_IMAGES['hero'])
                
                section_images.append({
                    "primary": primary_url,
                    "secondary": secondary_url,
                    "fallback": fallback_url,
                    "alt": f"Professional {keyword} imagery for AI engineer portfolio {section}",
                    "keyword": keyword
                })
            
            assets[section] = section_images
        
        return assets
    
    def _generate_seed(self, input_string: str) -> int:
        """Generate a consistent seed for image selection"""
        return int(hashlib.md5(input_string.encode()).hexdigest()[:8], 16) % 10000
    
    def _build_unsplash_url(self, keyword: str, width: int, height: int, seed: int) -> str:
        """Build Unsplash Source URL with proper encoding"""
        encoded_keyword = quote(keyword.replace(' ', ','))
        return f"https://source.unsplash.com/{width}x{height}/?{encoded_keyword}&sig={seed}"
    
    def _build_picsum_url(self, width: int, height: int, seed: int) -> str:
        """Build Lorem Picsum URL as secondary source"""
        return f"https://picsum.photos/{width}/{height}?random={seed}"
    
    def validate_image_url(self, url: str) -> bool:
        """Validate if an image URL is accessible"""
        try:
            response = self.session.head(url, timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.warning(f"Image validation failed for {url}: {e}")
            return False
    
    def get_optimized_image_css(self) -> str:
        """Generate CSS for optimized image handling"""
        return """
        /* AI Engineer Portfolio Image System */
        .hero-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .professional-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .project-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .project-image:hover {
            transform: scale(1.05);
        }
        
        .skill-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
            opacity: 0.8;
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
            background: #f8f9fa;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        /* Responsive image handling */
        @media (max-width: 768px) {
            .hero-image {
                height: 300px;
            }
            
            .professional-image {
                height: 250px;
            }
            
            .project-image {
                height: 180px;
            }
        }
        
        /* Lazy loading optimization */
        .lazy-image {
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .lazy-image.loaded {
            opacity: 1;
        }
        """
    
    def get_project_specific_images(self, project_type: str, count: int = 1) -> List[Dict[str, str]]:
        """Get images specific to a project type"""
        
        project_keywords = {
            "computer_vision": ["computer vision", "image recognition", "opencv", "deep learning"],
            "nlp": ["natural language processing", "text analysis", "chatbot", "language model"],
            "recommendation": ["recommendation system", "machine learning", "data analysis", "algorithms"],
            "data_science": ["data science", "analytics", "visualization", "statistics"],
            "robotics": ["robotics", "automation", "artificial intelligence", "technology"],
            "deep_learning": ["deep learning", "neural networks", "tensorflow", "pytorch"]
        }
        
        keywords = project_keywords.get(project_type, ["artificial intelligence", "machine learning"])
        images = []
        
        for i in range(count):
            keyword = keywords[i % len(keywords)]
            seed = self._generate_seed(f"{project_type}_{i}")
            
            images.append({
                "primary": self._build_unsplash_url(keyword, 350, 200, seed),
                "secondary": self._build_picsum_url(350, 200, seed),
                "fallback": self.FALLBACK_IMAGES["projects"],
                "alt": f"{project_type.replace('_', ' ').title()} project visualization",
                "keyword": keyword
            })
        
        return images