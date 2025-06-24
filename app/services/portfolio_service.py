"""Portfolio service for handling business logic and external integrations"""

import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from pathlib import Path

from nicegui import ui
from app.core.config import settings

logger = logging.getLogger(__name__)


class PortfolioService:
    """Service class for portfolio-related operations"""
    
    def __init__(self):
        self.resume_path = Path(settings.resume_path) / settings.resume_filename
        
    def send_contact_message(self, name: str, email: str, subject: str, message: str) -> bool:
        """Send contact form message via email"""
        
        # Validate inputs
        if not all([name, email, subject, message]):
            ui.notify("Please fill in all fields", type="negative")
            return False
        
        # For demo purposes, we'll just show a success notification
        # In production, you would integrate with an email service
        try:
            # Simulate email sending
            self._simulate_email_send(name, email, subject, message)
            
            ui.notify(
                f"Thank you {name}! Your message has been sent successfully. I'll get back to you soon!",
                type="positive",
                timeout=5000
            )
            return True
            
        except Exception as e:
            logger.error(f"Failed to send contact message: {e}")
            ui.notify("Sorry, there was an error sending your message. Please try again later.", type="negative")
            return False
    
    def _simulate_email_send(self, name: str, email: str, subject: str, message: str):
        """Simulate email sending (replace with actual email service in production)"""
        
        # Log the contact attempt
        logger.info(f"Contact form submission from {name} ({email}): {subject}")
        
        # In production, you would use services like:
        # - SendGrid
        # - AWS SES
        # - Mailgun
        # - SMTP server
        
        if settings.smtp_server and settings.smtp_username and settings.smtp_password:
            self._send_actual_email(name, email, subject, message)
        else:
            # For demo, just log the message
            logger.info(f"Demo mode - Contact message: {message}")
    
    def _send_actual_email(self, name: str, email: str, subject: str, message: str):
        """Send actual email using SMTP (if configured)"""
        
        try:
            msg = MIMEMultipart()
            msg['From'] = settings.smtp_username
            msg['To'] = settings.contact_email
            msg['Subject'] = f"Portfolio Contact: {subject}"
            
            body = f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(settings.smtp_server, settings.smtp_port)
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            text = msg.as_string()
            server.sendmail(settings.smtp_username, settings.contact_email, text)
            server.quit()
            
            logger.info(f"Email sent successfully from {email}")
            
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            raise
    
    def download_resume(self):
        """Handle resume download"""
        
        # Check if resume file exists
        if self.resume_path.exists():
            # In a real application, you would serve the file
            ui.notify("Resume download started! (Demo mode - file would be downloaded)", type="positive")
            logger.info("Resume download requested")
        else:
            # Create a placeholder resume for demo
            self._create_demo_resume()
            ui.notify("Demo resume created and download started!", type="positive")
    
    def _create_demo_resume(self):
        """Create a demo resume file"""
        
        # Ensure directory exists
        self.resume_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create a simple text resume for demo
        resume_content = """
AI ENGINEER RESUME
==================

CONTACT INFORMATION
-------------------
Name: AI Engineer
Email: contact@ai-engineer.dev
LinkedIn: linkedin.com/in/ai-engineer
GitHub: github.com/ai-engineer

SUMMARY
-------
Passionate AI Engineer with 5+ years of experience in developing and deploying 
machine learning solutions at scale. Expertise in computer vision, NLP, and 
predictive analytics.

TECHNICAL SKILLS
----------------
• Machine Learning: Scikit-learn, XGBoost, LightGBM
• Deep Learning: TensorFlow, PyTorch, Keras
• MLOps: Docker, Kubernetes, MLflow, AWS/GCP
• Data Engineering: Apache Spark, Airflow, PostgreSQL
• Programming: Python, SQL, JavaScript, Go

EXPERIENCE
----------
Senior AI Engineer | TechCorp Inc. | 2021 - Present
• Led team of 8 engineers developing ML features for 50M+ users
• Improved model accuracy by 23% through advanced feature engineering
• Reduced inference latency by 40% through optimization

Machine Learning Engineer | DataTech Solutions | 2019 - 2021
• Developed computer vision models for autonomous vehicles
• Built real-time data pipelines handling 1TB+ daily volume
• Mentored junior engineers and established ML coding standards

EDUCATION
---------
M.S. Computer Science, Specialization in AI | Stanford University | 2019
B.S. Computer Science | UC Berkeley | 2017

CERTIFICATIONS
--------------
• AWS Certified Machine Learning - Specialty
• Google Cloud Professional ML Engineer
• TensorFlow Developer Certificate
        """
        
        try:
            with open(self.resume_path, 'w') as f:
                f.write(resume_content)
            logger.info(f"Demo resume created at {self.resume_path}")
        except Exception as e:
            logger.error(f"Failed to create demo resume: {e}")
    
    def get_portfolio_stats(self) -> dict:
        """Get portfolio statistics for display"""
        
        return {
            "years_experience": 5,
            "projects_completed": 25,
            "models_deployed": 15,
            "users_impacted": "50M+",
            "accuracy_improvement": "23%",
            "latency_reduction": "40%"
        }
    
    def get_featured_projects(self) -> list:
        """Get featured projects data"""
        
        return [
            {
                "title": "Intelligent Document Processing System",
                "description": "End-to-end document processing using computer vision and NLP with 95% accuracy",
                "technologies": ["PyTorch", "OpenCV", "Transformers", "FastAPI"],
                "metrics": "95% accuracy, 1000+ documents/hour",
                "github_url": "https://github.com/ai-engineer/document-processing",
                "demo_url": "https://demo.ai-engineer.dev/document-processing"
            },
            {
                "title": "Real-time Recommendation Engine",
                "description": "Scalable recommendation system serving 10M+ users with sub-100ms latency",
                "technologies": ["TensorFlow", "Redis", "Kafka", "Kubernetes"],
                "metrics": "10M+ users, <100ms latency",
                "github_url": "https://github.com/ai-engineer/recommendation-engine",
                "demo_url": "https://demo.ai-engineer.dev/recommendations"
            },
            {
                "title": "Conversational AI Assistant",
                "description": "Intelligent chatbot using LLMs and RAG for technical query responses",
                "technologies": ["LangChain", "OpenAI API", "Vector DB", "Streamlit"],
                "metrics": "90% user satisfaction, 24/7 availability",
                "github_url": "https://github.com/ai-engineer/ai-assistant",
                "demo_url": "https://demo.ai-engineer.dev/ai-assistant"
            }
        ]
    
    def get_skills_data(self) -> dict:
        """Get skills data with proficiency levels"""
        
        return {
            "Machine Learning": {
                "proficiency": 95,
                "technologies": ["Scikit-learn", "XGBoost", "LightGBM", "Feature Engineering"],
                "years": 5
            },
            "Deep Learning": {
                "proficiency": 90,
                "technologies": ["TensorFlow", "PyTorch", "Keras", "Transformers"],
                "years": 4
            },
            "MLOps & Deployment": {
                "proficiency": 85,
                "technologies": ["Docker", "Kubernetes", "MLflow", "AWS/GCP"],
                "years": 3
            },
            "Data Engineering": {
                "proficiency": 80,
                "technologies": ["Apache Spark", "Airflow", "PostgreSQL", "Redis"],
                "years": 4
            }
        }