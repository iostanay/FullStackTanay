from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Security headers for production
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# Sample data for the iOS developer with 10 years experience
developer_data = {
    "name": "Tanay Bhattacharjee",
    "title": "Senior iOS Developer",
    "experience": "10+ Years",
    "location": "San Francisco, CA",
    "email": "tanay.bhattacharjee@email.com",
    "phone": "+1 (415) 555-0123",
    "github": "github.com/tanaybhattacharjee",
    "linkedin": "linkedin.com/in/tanaybhattacharjee",
    "about": "Passionate iOS developer with over 10 years of experience building high-quality mobile applications. Specialized in Swift, SwiftUI, and iOS architecture patterns. Led development teams and delivered apps used by millions of users.",
    "skills": {
        "languages": ["Swift", "Objective-C", "Python", "JavaScript","dfff"],
        "frameworks": ["SwiftUI", "UIKit", "Core Data", "Core Animation", "ARKit", "Core ML"],
        "tools": ["Xcode", "Git", "Jenkins", "Fastlane", "CocoaPods", "Swift Package Manager"],
        "architectures": ["MVVM", "MVC", "VIPER", "Clean Architecture", "TDD"],
        "platforms": ["iOS", "watchOS", "tvOS", "macOS"]
    },
    "experience": [
        {
            "company": "TechCorp Inc.",
            "position": "Senior iOS Developer",
            "duration": "2020 - Present",
            "description": "Lead iOS development for flagship products with 10M+ users. Implemented SwiftUI migration, improved app performance by 40%, and mentored junior developers.",
            "achievements": ["Reduced crash rate by 60%", "Implemented CI/CD pipeline", "Led team of 5 developers"]
        },
        {
            "company": "MobileStartup",
            "position": "iOS Developer",
            "duration": "2018 - 2020",
            "description": "Built and launched 3 successful iOS apps from concept to App Store. Handled full development lifecycle including UI/UX design and backend integration.",
            "achievements": ["2 apps reached top 100 in App Store", "Improved user retention by 35%", "Implemented advanced analytics"]
        },
        {
            "company": "AppStudio",
            "position": "Junior iOS Developer",
            "duration": "2015 - 2018",
            "description": "Developed iOS apps for various clients across different industries. Gained expertise in UIKit, Core Data, and third-party integrations.",
            "achievements": ["Delivered 15+ client projects", "Mastered Core Data optimization", "Learned advanced iOS patterns"]
        }
    ],
    "projects": [
        {
            "name": "HealthTracker Pro",
            "description": "Comprehensive health monitoring app with Apple Health integration",
            "technologies": ["SwiftUI", "HealthKit", "Core Data", "CloudKit"],
            "features": ["Real-time health monitoring", "Custom dashboards", "Apple Watch companion"],
            "app_store_rating": "4.8/5",
            "downloads": "500K+",
            "app_store_link": "https://apps.apple.com/app/healthtracker-pro/id1234567890",
            "app_icon": "/static/images/healthtracker-icon.svg",
            "screenshots": [
                "/static/images/healthtracker-ss1.svg",
                "/static/images/healthtracker-ss2.svg",
                "/static/images/healthtracker-ss3.svg"
            ],
            "app_category": "Health & Fitness",
            "release_date": "2023",
            "app_size": "45.2 MB"
        },
        {
            "name": "FinanceFlow",
            "description": "Personal finance management app with AI-powered insights",
            "technologies": ["Swift", "UIKit", "Core ML", "Firebase"],
            "features": ["Expense tracking", "Budget planning", "Investment insights"],
            "app_store_rating": "4.6/5",
            "downloads": "200K+",
            "app_store_link": "https://apps.apple.com/app/financeflow/id0987654321",
            "app_icon": "/static/images/financeflow-icon.svg",
            "screenshots": [
                "/static/images/financeflow-ss1.svg",
                "/static/images/financeflow-ss2.svg",
                "/static/images/financeflow-ss3.svg"
            ],
            "app_category": "Finance",
            "release_date": "2022",
            "app_size": "32.8 MB"
        },
        {
            "name": "TaskMaster",
            "description": "Productivity app with team collaboration features",
            "technologies": ["SwiftUI", "Combine", "CloudKit", "Push Notifications"],
            "features": ["Task management", "Team collaboration", "Real-time sync"],
            "app_store_rating": "4.7/5",
            "downloads": "150K+",
            "app_store_link": "https://apps.apple.com/app/taskmaster/id1122334455",
            "app_icon": "/static/images/taskmaster-icon.svg",
            "screenshots": [
                "/static/images/taskmaster-ss1.svg",
                "/static/images/taskmaster-ss2.svg",
                "/static/images/taskmaster-ss3.svg"
            ],
            "app_category": "Productivity",
            "release_date": "2023",
            "app_size": "28.5 MB"
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Science in Computer Science",
            "school": "Stanford University",
            "year": "2015"
        }
    ],
    "certifications": [
        "Apple Certified Developer",
        "AWS Certified Developer",
        "Google Cloud Platform Certified"
    ]
}

@app.route('/')
def home():
    return render_template('index.html', developer=developer_data)

@app.route('/about')
def about():
    return render_template('about.html', developer=developer_data)

@app.route('/experience')
def experience():
    return render_template('experience.html', developer=developer_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', developer=developer_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', developer=developer_data)

@app.route('/api/developer')
def api_developer():
    return jsonify(developer_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port) 