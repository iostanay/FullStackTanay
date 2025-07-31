#!/usr/bin/env python3
"""
Start script for iOS Developer Portfolio
Uses Gunicorn for production, Flask dev server for development
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Check if we're in production (Railway sets PORT)
    if os.environ.get('PORT'):
        # Production: Use Gunicorn
        print("🚀 Starting production server with Gunicorn...")
        print("📝 Use: gunicorn app:app -c gunicorn.conf.py")
        print("🌐 Your app will be available at: http://localhost:8000")
        print("⚠️  Don't use 'python app.py' in production!")
        sys.exit(0)
    else:
        # Development: Use Flask dev server
        print("🔧 Starting development server...")
        print("🌐 Your app will be available at: http://localhost:8000")
        app.run(debug=True, host='0.0.0.0', port=8000) 