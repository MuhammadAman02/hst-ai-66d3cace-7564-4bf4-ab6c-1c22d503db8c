"""Reusable UI components for the AI Engineer Portfolio"""

from nicegui import ui
from typing import Dict, List, Any
from app.core.assets import ProfessionalAssetManager
from app.services.portfolio_service import PortfolioService


class HeroSection:
    """Hero section component with professional imagery and CTA"""
    
    def __init__(self, assets: Dict[str, List[Dict[str, str]]]):
        self.assets = assets
    
    def render(self):
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
                with ui.element('div').classes('cta-buttons'):
                    ui.button('View My Work', 
                             on_click=lambda: ui.run_javascript('document.querySelector(".projects-section").scrollIntoView({behavior: "smooth"})')
                             ).classes('btn-primary')
                    ui.button('Download Resume', 
                             on_click=lambda: PortfolioService().download_resume()
                             ).classes('btn-secondary')


class AboutSection:
    """About section with professional information and image"""
    
    def __init__(self, assets: Dict[str, List[Dict[str, str]]]):
        self.assets = assets
    
    def render(self):
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
                    with ui.column().classes('flex-1'):
                        ui.image(self.assets['professional'][0]['primary']).classes('professional-image')


class SkillsSection:
    """Skills section with technology cards and proficiency indicators"""
    
    def __init__(self, portfolio_service: PortfolioService):
        self.portfolio_service = portfolio_service
    
    def render(self):
        """Render the skills section"""
        skills_data = self.portfolio_service.get_skills_data()
        
        with ui.element('section').classes('section').style('background: #f8f9fa;'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Technical Expertise</h2>')
                with ui.element('div').classes('skills-grid'):
                    
                    for skill_name, skill_info in skills_data.items():
                        with ui.element('div').classes('skill-card'):
                            # Skill icon based on category
                            icon_map = {
                                "Machine Learning": "fas fa-brain",
                                "Deep Learning": "fas fa-network-wired",
                                "MLOps & Deployment": "fas fa-cloud",
                                "Data Engineering": "fas fa-database"
                            }
                            
                            ui.html(f'<i class="{icon_map.get(skill_name, "fas fa-cog")} skill-icon"></i>')
                            ui.html(f'<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">{skill_name}</h3>')
                            
                            # Proficiency bar
                            with ui.element('div').style('margin-bottom: 1rem;'):
                                ui.html(f'<div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;"><span>Proficiency</span><span>{skill_info["proficiency"]}%</span></div>')
                                with ui.element('div').style('background: #e0e0e0; height: 8px; border-radius: 4px; overflow: hidden;'):
                                    ui.element('div').style(f'background: linear-gradient(45deg, #667eea, #764ba2); height: 100%; width: {skill_info["proficiency"]}%; transition: width 0.3s ease;')
                            
                            # Technologies
                            with ui.element('div').style('display: flex; flex-wrap: wrap; gap: 0.5rem;'):
                                for tech in skill_info["technologies"]:
                                    ui.html(f'<span class="tech-tag">{tech}</span>')


class ProjectsSection:
    """Projects section with project cards and details"""
    
    def __init__(self, assets: Dict[str, List[Dict[str, str]]], portfolio_service: PortfolioService):
        self.assets = assets
        self.portfolio_service = portfolio_service
    
    def render(self):
        """Render the projects section"""
        projects = self.portfolio_service.get_featured_projects()
        
        with ui.element('section').classes('section projects-section'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Featured Projects</h2>')
                with ui.element('div').classes('projects-grid'):
                    
                    for i, project in enumerate(projects):
                        with ui.element('div').classes('project-card'):
                            # Use project-specific image
                            image_index = i % len(self.assets['projects'])
                            ui.image(self.assets['projects'][image_index]['primary']).classes('project-image')
                            
                            with ui.element('div').classes('project-content'):
                                ui.html(f'<h3 class="project-title">{project["title"]}</h3>')
                                ui.html(f'<p class="project-description">{project["description"]}</p>')
                                
                                # Metrics
                                ui.html(f'<p style="color: #667eea; font-weight: 500; margin-bottom: 1rem;">📊 {project["metrics"]}</p>')
                                
                                # Technologies
                                with ui.element('div').classes('project-tech'):
                                    for tech in project["technologies"]:
                                        ui.html(f'<span class="tech-tag">{tech}</span>')
                                
                                # Action buttons
                                with ui.row().classes('gap-2 mt-4'):
                                    ui.link('View Code', project["github_url"], new_tab=True).classes('btn-primary').style('text-decoration: none; padding: 8px 16px; font-size: 0.9rem;')
                                    ui.link('Live Demo', project["demo_url"], new_tab=True).classes('btn-secondary').style('text-decoration: none; padding: 8px 16px; font-size: 0.9rem;')


class ExperienceSection:
    """Experience section with timeline and achievements"""
    
    def render(self):
        """Render the experience section"""
        with ui.element('section').classes('section').style('background: #f8f9fa;'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Professional Experience</h2>')
                with ui.column().classes('w-full max-w-4xl mx-auto'):
                    
                    # Experience entries
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
    
    def __init__(self, portfolio_service: PortfolioService):
        self.portfolio_service = portfolio_service
    
    def render(self):
        """Render the contact section"""
        with ui.element('section').classes('section contact-section'):
            with ui.element('div').classes('portfolio-container'):
                ui.html('<h2 class="section-title">Let\'s Connect</h2>')
                with ui.element('div').classes('contact-form'):
                    ui.html('<p style="text-align: center; margin-bottom: 2rem; font-size: 1.1rem;">Ready to discuss your next AI project? Let\'s talk!</p>')
                    
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
                                 on_click=lambda: self.portfolio_service.send_contact_message(
                                     name_input.value, email_input.value, 
                                     subject_input.value, message_input.value
                                 )).classes('btn-primary').style('width: 100%; margin-top: 1rem;')
                    
                    # Social Links
                    with ui.row().classes('justify-center gap-4 mt-8'):
                        ui.link('LinkedIn', 'https://linkedin.com/in/ai-engineer', new_tab=True).classes('btn-secondary')
                        ui.link('GitHub', 'https://github.com/ai-engineer', new_tab=True).classes('btn-secondary')
                        ui.link('Medium', 'https://medium.com/@ai-engineer', new_tab=True).classes('btn-secondary')