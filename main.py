"""
Production-ready AI Engineer Portfolio Application with:
✓ Professional interactive portfolio with integrated imagery
✓ Skills showcase with AI/ML technology visualizations
✓ Project galleries with detailed case studies
✓ Contact system with downloadable resume
✓ Real-time animations and smooth user experience
✓ Responsive design optimized for all devices
✓ Zero-configuration deployment readiness
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from nicegui import ui, app
from app.core.config import settings
from app.core.assets import ProfessionalAssetManager
from app.services.portfolio_service import PortfolioService
from app.components.portfolio_components import (
    HeroSection, AboutSection, SkillsSection, 
    ProjectsSection, ExperienceSection, ContactSection
)

# Initialize services
asset_manager = ProfessionalAssetManager()
portfolio_service = PortfolioService()

# Configure NiceGUI app
app.add_static_files('/static', 'app/static')

@ui.page('/')
async def portfolio_page():
    """Main portfolio page with all sections"""
    
    # Load professional assets for AI engineer portfolio
    assets = asset_manager.get_ai_engineer_assets()
    
    # Custom CSS for portfolio
    ui.add_head_html('''
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="AI Engineer Portfolio - Machine Learning, Deep Learning, and AI Solutions">
    <meta name="keywords" content="AI Engineer, Machine Learning, Deep Learning, Python, TensorFlow, PyTorch">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    ''')
    
    ui.add_css('''
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #333;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .portfolio-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .hero-section {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .hero-background {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6));
        z-index: 1;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 800px;
        padding: 2rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    .hero-description {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        opacity: 0.9;
        animation: fadeInUp 1s ease-out 0.6s both;
    }
    
    .cta-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        animation: fadeInUp 1s ease-out 0.9s both;
    }
    
    .btn-primary {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 12px 30px;
        border: none;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
    }
    
    .btn-secondary {
        background: transparent;
        color: white;
        padding: 12px 30px;
        border: 2px solid white;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .btn-secondary:hover {
        background: white;
        color: #333;
        transform: translateY(-2px);
    }
    
    .section {
        padding: 80px 0;
        background: white;
    }
    
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 3rem;
        color: #333;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .skill-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .skill-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .skill-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .project-card {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .project-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    .project-content {
        padding: 1.5rem;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .project-description {
        color: #666;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .project-tech {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .tech-tag {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .contact-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .contact-form {
        max-width: 600px;
        margin: 0 auto;
        background: rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .form-group {
        margin-bottom: 1.5rem;
    }
    
    .form-input {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        background: rgba(255,255,255,0.9);
        font-size: 1rem;
    }
    
    .form-textarea {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        background: rgba(255,255,255,0.9);
        font-size: 1rem;
        min-height: 120px;
        resize: vertical;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .cta-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .skills-grid,
        .projects-grid {
            grid-template-columns: 1fr;
        }
        
        .section {
            padding: 60px 0;
        }
    }
    ''')
    
    # Hero Section
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
                ui.button('View My Work', on_click=lambda: ui.run_javascript('document.querySelector(".projects-section").scrollIntoView({behavior: "smooth"})')).classes('btn-primary')
                ui.button('Download Resume', on_click=lambda: portfolio_service.download_resume()).classes('btn-secondary')
    
    # About Section
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
                    ui.image(assets['professional'][0]['primary']).classes('w-full rounded-lg shadow-lg').style('max-width: 400px; height: 300px; object-fit: cover;')
    
    # Skills Section
    with ui.element('section').classes('section').style('background: #f8f9fa;'):
        with ui.element('div').classes('portfolio-container'):
            ui.html('<h2 class="section-title">Technical Expertise</h2>')
            with ui.element('div').classes('skills-grid'):
                
                # Machine Learning
                with ui.element('div').classes('skill-card'):
                    ui.html('<i class="fas fa-brain skill-icon"></i>')
                    ui.html('<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">Machine Learning</h3>')
                    ui.html('''
                    <p style="color: #666; margin-bottom: 1rem;">
                        Advanced expertise in supervised, unsupervised, and reinforcement learning algorithms.
                    </p>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        <span class="tech-tag">Scikit-learn</span>
                        <span class="tech-tag">XGBoost</span>
                        <span class="tech-tag">LightGBM</span>
                        <span class="tech-tag">Feature Engineering</span>
                    </div>
                    ''')
                
                # Deep Learning
                with ui.element('div').classes('skill-card'):
                    ui.html('<i class="fas fa-network-wired skill-icon"></i>')
                    ui.html('<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">Deep Learning</h3>')
                    ui.html('''
                    <p style="color: #666; margin-bottom: 1rem;">
                        Building and optimizing neural networks for computer vision and NLP applications.
                    </p>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        <span class="tech-tag">TensorFlow</span>
                        <span class="tech-tag">PyTorch</span>
                        <span class="tech-tag">Keras</span>
                        <span class="tech-tag">Transformers</span>
                    </div>
                    ''')
                
                # MLOps & Deployment
                with ui.element('div').classes('skill-card'):
                    ui.html('<i class="fas fa-cloud skill-icon"></i>')
                    ui.html('<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">MLOps & Deployment</h3>')
                    ui.html('''
                    <p style="color: #666; margin-bottom: 1rem;">
                        End-to-end ML pipeline development and production deployment at scale.
                    </p>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        <span class="tech-tag">Docker</span>
                        <span class="tech-tag">Kubernetes</span>
                        <span class="tech-tag">MLflow</span>
                        <span class="tech-tag">AWS/GCP</span>
                    </div>
                    ''')
                
                # Data Engineering
                with ui.element('div').classes('skill-card'):
                    ui.html('<i class="fas fa-database skill-icon"></i>')
                    ui.html('<h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem;">Data Engineering</h3>')
                    ui.html('''
                    <p style="color: #666; margin-bottom: 1rem;">
                        Building robust data pipelines and infrastructure for ML workloads.
                    </p>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        <span class="tech-tag">Apache Spark</span>
                        <span class="tech-tag">Airflow</span>
                        <span class="tech-tag">PostgreSQL</span>
                        <span class="tech-tag">Redis</span>
                    </div>
                    ''')
    
    # Projects Section
    with ui.element('section').classes('section projects-section'):
        with ui.element('div').classes('portfolio-container'):
            ui.html('<h2 class="section-title">Featured Projects</h2>')
            with ui.element('div').classes('projects-grid'):
                
                # Project 1: Computer Vision System
                with ui.element('div').classes('project-card'):
                    ui.image(assets['projects'][0]['primary']).classes('project-image')
                    with ui.element('div').classes('project-content'):
                        ui.html('<h3 class="project-title">Intelligent Document Processing System</h3>')
                        ui.html('''
                        <p class="project-description">
                            Built an end-to-end document processing system using computer vision and NLP 
                            to extract and classify information from unstructured documents with 95% accuracy.
                        </p>
                        ''')
                        with ui.element('div').classes('project-tech'):
                            ui.html('<span class="tech-tag">PyTorch</span>')
                            ui.html('<span class="tech-tag">OpenCV</span>')
                            ui.html('<span class="tech-tag">Transformers</span>')
                            ui.html('<span class="tech-tag">FastAPI</span>')
                        ui.button('View Details', on_click=lambda: ui.notify('Project details would open here')).classes('btn-primary').style('margin-top: 1rem;')
                
                # Project 2: Recommendation Engine
                with ui.element('div').classes('project-card'):
                    ui.image(assets['projects'][1]['primary']).classes('project-image')
                    with ui.element('div').classes('project-content'):
                        ui.html('<h3 class="project-title">Real-time Recommendation Engine</h3>')
                        ui.html('''
                        <p class="project-description">
                            Developed a scalable recommendation system serving 10M+ users with sub-100ms 
                            latency using collaborative filtering and deep learning techniques.
                        </p>
                        ''')
                        with ui.element('div').classes('project-tech'):
                            ui.html('<span class="tech-tag">TensorFlow</span>')
                            ui.html('<span class="tech-tag">Redis</span>')
                            ui.html('<span class="tech-tag">Kafka</span>')
                            ui.html('<span class="tech-tag">Kubernetes</span>')
                        ui.button('View Details', on_click=lambda: ui.notify('Project details would open here')).classes('btn-primary').style('margin-top: 1rem;')
                
                # Project 3: NLP Chatbot
                with ui.element('div').classes('project-card'):
                    ui.image(assets['projects'][2]['primary']).classes('project-image')
                    with ui.element('div').classes('project-content'):
                        ui.html('<h3 class="project-title">Conversational AI Assistant</h3>')
                        ui.html('''
                        <p class="project-description">
                            Created an intelligent chatbot using large language models and RAG architecture 
                            to provide accurate responses to complex technical queries.
                        </p>
                        ''')
                        with ui.element('div').classes('project-tech'):
                            ui.html('<span class="tech-tag">LangChain</span>')
                            ui.html('<span class="tech-tag">OpenAI API</span>')
                            ui.html('<span class="tech-tag">Vector DB</span>')
                            ui.html('<span class="tech-tag">Streamlit</span>')
                        ui.button('View Details', on_click=lambda: ui.notify('Project details would open here')).classes('btn-primary').style('margin-top: 1rem;')
    
    # Experience Section
    with ui.element('section').classes('section').style('background: #f8f9fa;'):
        with ui.element('div').classes('portfolio-container'):
            ui.html('<h2 class="section-title">Professional Experience</h2>')
            with ui.column().classes('w-full max-w-4xl mx-auto'):
                
                # Experience 1
                with ui.card().classes('w-full mb-6 p-6'):
                    ui.html('''
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                        <div>
                            <h3 style="font-size: 1.4rem; font-weight: 600; color: #333;">Senior AI Engineer</h3>
                            <p style="color: #667eea; font-weight: 500; font-size: 1.1rem;">TechCorp Inc.</p>
                        </div>
                        <span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem;">2021 - Present</span>
                    </div>
                    <ul style="color: #555; line-height: 1.6; margin-left: 1rem;">
                        <li>Led a team of 8 engineers to develop ML-powered features serving 50M+ users</li>
                        <li>Improved model accuracy by 23% through advanced feature engineering and ensemble methods</li>
                        <li>Reduced inference latency by 40% through model optimization and efficient deployment strategies</li>
                        <li>Established MLOps practices reducing model deployment time from weeks to hours</li>
                    </ul>
                    ''')
                
                # Experience 2
                with ui.card().classes('w-full mb-6 p-6'):
                    ui.html('''
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                        <div>
                            <h3 style="font-size: 1.4rem; font-weight: 600; color: #333;">Machine Learning Engineer</h3>
                            <p style="color: #667eea; font-weight: 500; font-size: 1.1rem;">DataTech Solutions</p>
                        </div>
                        <span style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem;">2019 - 2021</span>
                    </div>
                    <ul style="color: #555; line-height: 1.6; margin-left: 1rem;">
                        <li>Developed computer vision models for autonomous vehicle perception systems</li>
                        <li>Built real-time data processing pipelines handling 1TB+ daily data volume</li>
                        <li>Collaborated with product teams to integrate ML capabilities into customer-facing applications</li>
                        <li>Mentored junior engineers and established coding standards for the ML team</li>
                    </ul>
                    ''')
    
    # Contact Section
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
                             on_click=lambda: portfolio_service.send_contact_message(
                                 name_input.value, email_input.value, 
                                 subject_input.value, message_input.value
                             )).classes('btn-primary').style('width: 100%; margin-top: 1rem;')
                
                # Social Links
                with ui.row().classes('justify-center gap-4 mt-8'):
                    ui.link('LinkedIn', 'https://linkedin.com/in/ai-engineer', new_tab=True).classes('btn-secondary')
                    ui.link('GitHub', 'https://github.com/ai-engineer', new_tab=True).classes('btn-secondary')
                    ui.link('Medium', 'https://medium.com/@ai-engineer', new_tab=True).classes('btn-secondary')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host=settings.host,
        port=settings.port,
        title="AI Engineer Portfolio - Machine Learning & Deep Learning Specialist",
        favicon="🤖",
        reload=settings.debug,
        show=True
    )