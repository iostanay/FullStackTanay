#!/usr/bin/env python3
"""
Test script to verify deployment configuration
"""
import os
import sys
from app import app

def test_app_import():
    """Test that the app can be imported and configured"""
    try:
        # Test that the app exists
        assert app is not None
        print("✅ App import successful")
        
        # Test that the app has the expected routes
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        expected_routes = ['/', '/about', '/experience', '/projects', '/contact', '/api/developer']
        
        for route in expected_routes:
            assert route in routes, f"Missing route: {route}"
        
        print("✅ All expected routes found")
        
        # Test environment variables
        port = os.environ.get('PORT', '8000')
        print(f"✅ PORT environment variable: {port}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing deployment configuration...")
    success = test_app_import()
    
    if success:
        print("✅ All tests passed! Ready for deployment.")
        sys.exit(0)
    else:
        print("❌ Tests failed! Please fix issues before deploying.")
        sys.exit(1) 