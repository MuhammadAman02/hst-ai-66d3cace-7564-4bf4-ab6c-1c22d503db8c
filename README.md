# 🤖 AI Engineer Portfolio

A professional, interactive portfolio application for AI Engineers built with NiceGUI, featuring modern design, project showcases, and integrated visual assets.

## ✨ Features

### 🎯 Core Functionality
- **Interactive Portfolio**: Modern, responsive design with smooth animations
- **Project Showcase**: Detailed project cards with technologies and live demos
- **Skills Visualization**: Technical expertise with proficiency indicators
- **Professional Experience**: Timeline-based experience showcase
- **Contact System**: Functional contact form with email integration
- **Resume Download**: Downloadable resume/CV functionality

### 🎨 Visual Excellence
- **Professional Imagery**: Automatically integrated AI/tech-focused images
- **Responsive Design**: Optimized for all devices and screen sizes
- **Modern UI/UX**: Clean, professional interface with gradient themes
- **Smooth Animations**: Engaging user experience with CSS animations
- **Accessibility**: WCAG-compliant design with keyboard navigation

### 🚀 Technical Highlights
- **Zero-Configuration**: Runs immediately without setup
- **Production-Ready**: Docker containerization and deployment configs
- **Performance Optimized**: Fast loading with lazy image loading
- **Type Safety**: Comprehensive type hints throughout
- **Error Handling**: Graceful degradation and user feedback

## 🛠️ Technology Stack

- **Framework**: NiceGUI (Python-based web framework)
- **Backend**: Python 3.11+ with async support
- **Styling**: Modern CSS with custom design system
- **Images**: Unsplash API integration with fallbacks
- **Deployment**: Docker with multi-stage builds
- **Configuration**: Environment-based settings

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**:
```bash
git clone <repository-url>
cd ai-engineer-portfolio
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment** (optional):
```bash
cp .env.example .env
# Edit .env with your personal information
```

4. **Run the application**:
```bash
python main.py
```

5. **Open your browser**:
Navigate to `http://localhost:8080`

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
docker-compose up -d
```

### Using Docker directly
```bash
# Build the image
docker build -t ai-engineer-portfolio .

# Run the container
docker run -p 8080:8080 ai-engineer-portfolio
```

## 📁 Project Structure

```
ai-engineer-portfolio/
├── app/
│   ├── core/                 # Core configuration and utilities
│   │   ├── config.py        # Application settings
│   │   └── assets.py        # Visual asset management
│   ├── services/            # Business logic services
│   │   └── portfolio_service.py
│   ├── components/          # Reusable UI components
│   │   └── portfolio_components.py
│   └── static/              # Static assets
│       ├── css/            # Stylesheets
│       └── documents/      # Downloadable files
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-service orchestration
└── README.md               # This file
```

## 🎨 Customization

### Personal Information
Edit the following files to customize with your information:

1. **Portfolio Content** (`main.py`):
   - Update hero section text
   - Modify about section content
   - Add your projects and experience

2. **Configuration** (`.env`):
   - Social media links
   - Contact information
   - Email settings

3. **Assets** (`app/core/assets.py`):
   - Customize image categories
   - Add project-specific images

### Styling
- **CSS Variables**: Modify `app/static/css/main.css` for colors and spacing
- **Components**: Update `app/components/portfolio_components.py` for layout changes

## 📧 Contact Form Setup

To enable the contact form email functionality:

1. **Configure SMTP settings** in `.env`:
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

2. **For Gmail**: Use an App Password instead of your regular password

3. **Alternative Services**: The code supports any SMTP server (SendGrid, Mailgun, etc.)

## 🔧 Development

### Adding New Sections
1. Create a new component in `app/components/portfolio_components.py`
2. Add the component to the main page in `main.py`
3. Update CSS in `app/static/css/main.css` if needed

### Adding New Projects
Update the `get_featured_projects()` method in `app/services/portfolio_service.py`:

```python
{
    "title": "Your Project Name",
    "description": "Project description",
    "technologies": ["Tech1", "Tech2"],
    "metrics": "Key metrics",
    "github_url": "https://github.com/...",
    "demo_url": "https://demo.example.com"
}
```

## 📊 Performance

- **Load Time**: < 2 seconds initial load
- **Image Optimization**: Lazy loading with progressive enhancement
- **Caching**: Efficient asset caching strategies
- **Mobile Performance**: Optimized for mobile devices

## 🔒 Security

- **Input Validation**: All form inputs are validated
- **CORS Protection**: Proper CORS configuration
- **Environment Variables**: Sensitive data in environment files
- **Container Security**: Non-root user in Docker container

## 🌐 Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile Browsers**: iOS Safari, Chrome Mobile
- **Accessibility**: Screen reader compatible

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you have questions or need help:

1. **Documentation**: Check this README and code comments
2. **Issues**: Open an issue on GitHub
3. **Discussions**: Use GitHub Discussions for questions

## 🎯 Roadmap

- [ ] Blog integration
- [ ] Project filtering and search
- [ ] Dark/light theme toggle
- [ ] Multi-language support
- [ ] Analytics dashboard
- [ ] PDF resume generation
- [ ] Project case study pages

---

**Built with ❤️ for AI Engineers by AI Engineers**

*Showcase your AI expertise with a professional, modern portfolio that demonstrates your technical skills and project achievements.*