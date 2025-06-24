"""Portfolio UI components for the AI Engineer portfolio"""

from nicegui import ui
from typing import Dict, List, Any
from app.core.assets import ImageAsset


class HeroSection:
    """Hero section component with professional imagery"""
    
    @staticmethod
    def render(assets: Dict[str, List[ImageAsset]]):
        """Render the hero section"""
        with ui.element('div').classes('hero-section'):
            ui.element('div').classes('hero-background')
            with ui.element('div').classes('hero-content'):
                ui.html('<h1 class="hero-title">AI Engineer & ML Specialist</h1>')
                ui.html('<p class="hero-subtitle">Transforming Data into Intelligent Solutions</p>')
                ui.html('''
                <p class="hero-description">
                    Passionate about building cutting-edge AI systems that solve real-world problems. 
                    Specialized in machine learning, deep learning, and scalable AI architectures.
                </p>
                ''')


class AboutSection:
    """About section with professional imagery"""
    
    @staticmethod
    def render(assets: Dict[str, List[ImageAsset]]):
        """Render the about section"""
        with ui.element('section').classes('section'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">About Me</h2>')
                with ui.row().classes('w-full gap-8 items-center'):
                    with ui.column().classes('flex-1'):
                        ui.html('''
                        <div style="font-size: 1.1rem; line-height: 1.8; color: #555;">
                            <p style="margin-bottom: 1.5rem;">
                                I'm a passionate AI Engineer with 5+ years of experience in developing and deploying 
                                machine learning solutions at scale. My expertise spans across computer vision, 
                                natural language processing, and predictive analytics.
                            </p>
                            <p style="margin-bottom: 1.5rem;">
                                I've led cross-functional teams to deliver AI-powered products that have impacted 
                                millions of users, from recommendation systems to autonomous decision-making platforms.
                            </p>
                            <p>
                                When I'm not coding, you'll find me contributing to open-source projects, 
                                writing technical blogs, or exploring the latest research in AI/ML.
                            </p>
                        </div>
                        ''')


class SkillsSection:
    """Skills section with technology visualizations"""
    
    @staticmethod
    def render(assets: Dict[str, List[ImageAsset]]):
        """Render the skills section"""
        with ui.element('section').classes('section').style('background: #f8f9fa;'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Technical Expertise</h2>')
                with ui.element('div').classes('skills-grid'):
                    SkillsSection._render_skill_cards()
    
    @staticmethod
    def _render_skill_cards():
        """Render individual skill cards"""
        skills = [
            {
                "icon": "fas fa-brain",
                "title": "Machine Learning",
                "description": "Advanced expertise in supervised, unsupervised, and reinforcement learning algorithms.",
                "technologies": ["Scikit-learn", "XGBoost", "LightGBM", "Feature Engineering"]
            },
            {
                "icon": "fas fa-network-wired",
                "title": "Deep Learning",
                "description": "Building and optimizing neural networks for computer vision and NLP applications.",
                "technologies": ["TensorFlow", "PyTorch", "Keras", "Transformers"]
            },
            {
                "icon": "fas fa-cloud",
                "title": "MLOps & Deployment",
                "description": "End-to-end ML pipeline development and production deployment at scale.",
                "technologies": ["Docker", "Kubernetes", "MLflow", "AWS/GCP"]
            },
            {
                "icon": "fas fa-database",
                "title": "Data Engineering",
                "description": "Building robust data pipelines and infrastructure for ML workloads.",
                "technologies": ["Apache Spark", "Airflow", "PostgreSQL", "Redis"]
            }
        ]
        
        for skill in skills:
            with ui.element('div').classes('skill-card'):
                ui.html(f'<i class="{skill["icon"]} skill-icon"></i>')
                ui.html(f'<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">{skill["title"]}</h3>')
                ui.html(f'''
                <p style="color: #666; margin-bottom: 1rem;">
                    {skill["description"]}
                </p>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {"".join([f'<span class="tech-tag">{tech}</span>' for tech in skill["technologies"]])}
                </div>
                ''')


class ProjectsSection:
    """Projects section with interactive galleries"""
    
    @staticmethod
    def render(assets: Dict[str, List[ImageAsset]]):
        """Render the projects section"""
        with ui.element('section').classes('section projects-section'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Featured Projects</h2>')
                with ui.element('div').classes('projects-grid'):
                    ProjectsSection._render_project_cards(assets)
    
    @staticmethod
    def _render_project_cards(assets: Dict[str, List[ImageAsset]]):
        """Render individual project cards"""
        projects = [
            {
                "title": "Intelligent Document Processing System",
                "description": "Built an end-to-end document processing system using computer vision and NLP to extract and classify information from unstructured documents with 95% accuracy.",
                "technologies": ["PyTorch", "OpenCV", "Transformers", "FastAPI"],
                "image_index": 0
            },
            {
                "title": "Real-time Recommendation Engine",
                "description": "Developed a scalable recommendation system serving 10M+ users with sub-100ms latency using collaborative filtering and deep learning techniques.",
                "technologies": ["TensorFlow", "Redis", "Kafka", "Kubernetes"],
                "image_index": 1
            },
            {
                "title": "Conversational AI Assistant",
                "description": "Created an intelligent chatbot using large language models and RAG architecture to provide accurate responses to complex technical queries.",
                "technologies": ["LangChain", "OpenAI API", "Vector DB", "Streamlit"],
                "image_index": 2
            }
        ]
        
        project_assets = assets.get('projects', [])
        
        for i, project in enumerate(projects):
            with ui.element('div').classes('project-card'):
                # Use project image if available, otherwise use placeholder
                if i < len(project_assets):
                    ui.image(project_assets[i].primary_url).classes('project-image')
                else:
                    ui.image('https://via.placeholder.com/350x200/667eea/ffffff?text=AI+Project').classes('project-image')
                
                with ui.element('div').classes('project-content'):
                    ui.html(f'<h3 class="project-title">{project["title"]}</h3>')
                    ui.html(f'<p class="project-description">{project["description"]}</p>')
                    
                    with ui.element('div').classes('project-tech'):
                        for tech in project["technologies"]:
                            ui.html(f'<span class="tech-tag">{tech}</span>')
                    
                    ui.button('View Details', 
                             on_click=lambda p=project: ui.notify(f'Details for {p["title"]} would open here')
                             ).classes('btn-primary').style('margin-top: 1rem;')


class ExperienceSection:
    """Experience section with professional timeline"""
    
    @staticmethod
    def render():
        """Render the experience section"""
        with ui.element('section').classes('section').style('background: #f8f9fa;'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Professional Experience</h2>')
                with ui.column().classes('w-full max-w-4xl mx-auto'):
                    ExperienceSection._render_experience_cards()
    
    @staticmethod
    def _render_experience_cards():
        """Render individual experience cards"""
        experiences = [
            {
                "title": "Senior AI Engineer",
                "company": "TechCorp Inc.",
                "period": "2021 - Present",
                "achievements": [
                    "Led a team of 8 engineers to develop ML-powered features serving 50M+ users",
                    "Improved model accuracy by 23% through advanced feature engineering and ensemble methods",
                    "Reduced inference latency by 40% through model optimization and efficient deployment strategies",
                    "Established MLOps practices reducing model deployment time from weeks to hours"
                ]
            },
            {
                "title": "Machine Learning Engineer",
                "company": "DataTech Solutions",
                "period": "2019 - 2021",
                "achievements": [
                    "Developed computer vision models for autonomous vehicle perception systems",
                    "Built real-time data processing pipelines handling 1TB+ daily data volume",
                    "Collaborated with product teams to integrate ML capabilities into customer-facing applications",
                    "Mentored junior engineers and established coding standards for the ML team"
                ]
            }
        ]
        
        for exp in experiences:
            with ui.card().classes('w-full mb-6 p-6'):
                ui.html(f'''
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="font-size: 1.4rem; font-weight: 600; color: #333;">{exp["title"]}</h3>
                        <p style="color: #667eea; font-weight: 500; font-size: 1.1rem;">{exp["company"]}</p>
                    </div>
                    <span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem;">{exp["period"]}</span>
                </div>
                <ul style="color: #555; line-height: 1.6; margin-left: 1rem;">
                    {"".join([f"<li>{achievement}</li>" for achievement in exp["achievements"]])}
                </ul>
                ''')


class ContactSection:
    """Contact section with form and social links"""
    
    @staticmethod
    def render(portfolio_service):
        """Render the contact section"""
        with ui.element('section').classes('section contact-section'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Let\'s Connect</h2>')
                with ui.element('div').classes('contact-form'):
                    ui.html('<p style="text-align: center; margin-bottom: 2rem; font-size: 1.1rem;">Ready to discuss your next AI project? Let\'s talk!</p>')
                    
                    ContactSection._render_contact_form(portfolio_service)
                    ContactSection._render_social_links()
    
    @staticmethod
    def _render_contact_form(portfolio_service):
        """Render the contact form"""
        with ui.element('form'):
            with ui.element('div').classes('form-group'):
                name_input = ui.input('Your Name').classes('form-input').style('width: 100%;')
            
            with ui.element('div').classes('form-group'):
                email_input = ui.input('Your Email').classes('form-input').style('width: 100%;')
            
            with ui.element('div').classes('form-group'):
                subject_input = ui.input('Subject').classes('form-input').style('width: 100%;')
            
            with ui.element('div').classes('form-group'):
                message_input = ui.textarea('Your Message').classes('form-textarea').style('width: 100%;')
            
            ui.button('Send Message', 
                     on_click=lambda: portfolio_service.send_contact_message(
                         name_input.value, email_input.value, 
                         subject_input.value, message_input.value
                     )).classes('btn-primary').style('width: 100%; margin-top: 1rem;')
    
    @staticmethod
    def _render_social_links():
        """Render social media links"""
        with ui.row().classes('justify-center gap-4 mt-8'):
            ui.link('LinkedIn', 'https://linkedin.com/in/ai-engineer', new_tab=True).classes('btn-secondary')
            ui.link('GitHub', 'https://github.com/ai-engineer', new_tab=True).classes('btn-secondary')
            ui.link('Medium', 'https://medium.com/@ai-engineer', new_tab=True).classes('btn-secondary')