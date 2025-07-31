# iOS Developer Portfolio - Flask Application

A modern, responsive portfolio website for a senior iOS developer with 10+ years of experience, built with Flask and Bootstrap.

## Features

- **Modern Design**: Clean, professional design with iOS-inspired aesthetics
- **Responsive Layout**: Fully responsive design that works on all devices
- **Interactive Elements**: Smooth animations and hover effects
- **Comprehensive Sections**: Home, About, Experience, Projects, and Contact pages
- **Professional Content**: Detailed showcase of iOS development expertise

## Pages

### Home Page (`/`)
- Hero section with introduction
- Key statistics and achievements
- Technical skills showcase
- Featured projects preview
- Call-to-action sections

### About Page (`/about`)
- Personal story and background
- Detailed technical skills breakdown
- Education and certifications
- Key achievements and milestones

### Experience Page (`/experience`)
- Professional work history timeline
- Career highlights and statistics
- Technical evolution over 10 years
- Skills by experience level

### Projects Page (`/projects`)
- Detailed project showcase
- Project categories and technologies
- Development process explanation
- Project statistics

### Contact Page (`/contact`)
- Contact information
- Contact form
- Services offered
- Response time information

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5.3
- **Icons**: Font Awesome 6.4
- **Fonts**: Google Fonts (Inter)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ios-developer-portfolio
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## Project Structure

```
ios-developer-portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation and footer
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── experience.html   # Experience page
│   ├── projects.html     # Projects page
│   └── contact.html      # Contact page
└── static/               # Static files (CSS, JS, images)
    ├── css/
    ├── js/
    └── images/
```

## Customization

### Updating Developer Information

Edit the `developer_data` dictionary in `app.py` to customize:

- Personal information (name, title, contact details)
- Skills and technologies
- Work experience
- Projects and achievements
- Education and certifications

### Styling

The design uses CSS custom properties for easy theming:

```css
:root {
    --primary-color: #007AFF;    /* iOS blue */
    --secondary-color: #5856D6;  /* Purple accent */
    --accent-color: #FF2D92;     /* Pink accent */
    --dark-bg: #1C1C1E;         /* Dark background */
    --light-bg: #F2F2F7;        /* Light background */
    --text-primary: #1D1D1F;    /* Primary text */
    --text-secondary: #86868B;   /* Secondary text */
}
```

### Adding New Pages

1. Create a new template in `templates/`
2. Add a route in `app.py`
3. Update navigation in `base.html`

## Features for iOS Developer Portfolio

### Technical Skills Showcase
- Programming Languages: Swift, Objective-C, Python, JavaScript
- iOS Frameworks: SwiftUI, UIKit, Core Data, Core Animation, ARKit, Core ML
- Development Tools: Xcode, Git, Jenkins, Fastlane, CocoaPods, Swift Package Manager
- Architecture Patterns: MVVM, MVC, VIPER, Clean Architecture, TDD
- Platforms: iOS, watchOS, tvOS, macOS

### Project Showcase
- Health & Fitness apps with HealthKit integration
- Finance apps with Core ML and security features
- Productivity apps with CloudKit and real-time sync
- All projects include App Store ratings and download statistics

### Professional Experience
- 10+ years of iOS development experience
- Team leadership and mentoring
- Performance optimization expertise
- App Store success with millions of downloads

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:

- **Heroku**: Easy deployment with Git integration
- **PythonAnywhere**: Python-focused hosting
- **AWS/GCP**: Cloud hosting solutions
- **Docker**: Containerized deployment

### Environment Variables
Set the following environment variables for production:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or support, please contact:
- Email: alex.chen@email.com
- GitHub: github.com/alexchen-ios
- LinkedIn: linkedin.com/in/alexchen-ios

---

**Built with ❤️ for iOS developers who want to showcase their expertise professionally.** 