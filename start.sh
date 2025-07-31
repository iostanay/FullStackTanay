#!/bin/bash

echo "🚀 iOS Developer Portfolio - Server Starter"
echo "=========================================="

# Check if we're in production (Railway sets PORT)
if [ ! -z "$PORT" ]; then
    echo "🌐 Production mode detected"
    echo "📝 Starting with Gunicorn (production WSGI server)"
    echo "✅ No development server warnings!"
    gunicorn app:app -c gunicorn.conf.py
else
    echo "🔧 Development mode detected"
    echo "📝 Starting with Flask development server"
    echo "⚠️  This is for development only!"
    python app.py
fi 