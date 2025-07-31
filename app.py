from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
from database import db

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

# Contact Form API Endpoints
@app.route('/api/contacts', methods=['POST'])
def create_contact():
    """Create a new contact message"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Validation
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Add to database
        success = db.add_contact(name, email, message)
        
        if success:
            return jsonify({
                'message': 'Contact message sent successfully',
                'status': 'success'
            }), 201
        else:
            return jsonify({'error': 'Failed to save message'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """Get all contact messages (admin endpoint)"""
    try:
        limit = request.args.get('limit', 50, type=int)
        contacts = db.get_contacts(limit)
        
        return jsonify({
            'contacts': contacts,
            'count': len(contacts)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """Get a specific contact message by ID"""
    try:
        contact = db.get_contact_by_id(contact_id)
        
        if contact:
            return jsonify(contact), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """Delete a contact message by ID"""
    try:
        success = db.delete_contact(contact_id)
        
        if success:
            return jsonify({'message': 'Contact deleted successfully'}), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize database
    db.init_database()
    
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port) 