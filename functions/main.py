import firebase_functions
from firebase_functions import https_fn
from firebase_admin import initialize_app
import os
import sys

# Add the parent directory to the path so we can import our Flask app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Initialize Firebase Admin SDK
initialize_app()

@https_fn.on_request()
def flaskApp(req: https_fn.Request) -> https_fn.Response:
    """Cloud Function to serve Flask app"""
    
    # Set environment variables for Flask
    os.environ['FLASK_ENV'] = 'production'
    
    # Create a WSGI environment from the request
    environ = {
        'REQUEST_METHOD': req.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': req.path,
        'QUERY_STRING': req.query_string.decode('utf-8'),
        'SERVER_NAME': req.headers.get('host', 'localhost'),
        'SERVER_PORT': '80',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': req.get_body(),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Add headers
    for key, value in req.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    # Create a simple response class
    class Response:
        def __init__(self):
            self.status = '200 OK'
            self.headers = []
            self.body = []
        
        def __call__(self, environ, start_response):
            start_response(self.status, self.headers)
            return self.body
    
    # Call the Flask app
    response = Response()
    response = app(environ, response.__call__)
    
    # Convert the response to Firebase Functions format
    body = b''.join(response).decode('utf-8')
    
    return https_fn.Response(
        body,
        status=200,
        headers={'Content-Type': 'text/html'}
    ) 