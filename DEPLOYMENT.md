# Deployment Guide - iOS Developer Portfolio

This guide will help you deploy your Flask-based iOS developer portfolio to various platforms.

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the application**:
   Open your browser and navigate to `http://localhost:8000`

## Deployment Options

### 1. Heroku Deployment

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:
   ```bash
   heroku create your-portfolio-name
   ```

3. **Create Procfile** (create a file named `Procfile` in the root directory):
   ```
   web: gunicorn app:app
   ```

4. **Add gunicorn to requirements.txt**:
   ```
   gunicorn==21.2.0
   ```

5. **Deploy to Heroku**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### 2. PythonAnywhere Deployment

1. **Sign up for PythonAnywhere** (free tier available)

2. **Upload your files**:
   - Go to the Files tab
   - Upload your project files

3. **Create a new web app**:
   - Go to the Web tab
   - Click "Add a new web app"
   - Choose "Flask" and Python 3.9

4. **Configure the WSGI file**:
   - Edit the WSGI file to point to your app
   - Set the path to your app.py file

5. **Set up static files**:
   - Configure static files mapping in the Web tab

### 3. Vercel Deployment

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Create vercel.json** in the root directory:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

### 4. Railway Deployment

1. **Connect your GitHub repository** to Railway

2. **Railway will automatically detect** the Flask application

3. **Set environment variables** if needed:
   - `FLASK_ENV=production`
   - `PORT=8000`

4. **Deploy** - Railway will automatically deploy your app

## Environment Variables

For production deployment, set these environment variables:

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export PORT=8000
```

## Custom Domain Setup

### 1. Heroku Custom Domain

1. **Add custom domain**:
   ```bash
   heroku domains:add yourdomain.com
   ```

2. **Configure DNS**:
   - Add a CNAME record pointing to your Heroku app
   - Or add an A record for apex domains

### 2. SSL Certificate

Most platforms (Heroku, Vercel, Railway) provide automatic SSL certificates.

## Firebase Integration

The application includes Firebase Analytics integration. To customize:

1. **Update Firebase config** in `templates/base.html`
2. **Add Firebase services** as needed (Authentication, Firestore, etc.)
3. **Configure Firebase project** in the Firebase Console

## Performance Optimization

### 1. Static File Optimization

1. **Minify CSS and JS** files
2. **Enable gzip compression**
3. **Use CDN** for external libraries

### 2. Database Integration (Optional)

If you want to add a database for contact form submissions:

1. **Add SQLAlchemy** to requirements.txt
2. **Create database models**
3. **Update contact form** to save to database

### 3. Caching

Add Redis caching for better performance:

```python
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'redis'})
```

## Monitoring and Analytics

### 1. Firebase Analytics

- Page views are automatically tracked
- Custom events are set up for form submissions
- Project clicks are tracked

### 2. Google Analytics

- Basic page tracking is configured
- Custom events for user interactions

### 3. Error Monitoring

Consider adding Sentry for error monitoring:

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

## Security Considerations

1. **Environment Variables**: Never commit sensitive data
2. **HTTPS**: Always use HTTPS in production
3. **Input Validation**: The contact form includes basic validation
4. **Rate Limiting**: Consider adding rate limiting for the contact form

## Backup and Maintenance

1. **Regular backups** of your code repository
2. **Monitor application logs** for errors
3. **Update dependencies** regularly
4. **Test deployment** in staging environment first

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`
2. **Static files not loading**: Check file paths and permissions
3. **Firebase not working**: Verify configuration in base.html
4. **Form not submitting**: Check JavaScript console for errors

### Debug Mode

For debugging, enable debug mode:

```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

## Support

For deployment issues:

1. Check the platform's documentation
2. Review application logs
3. Test locally first
4. Check environment variables

---

**Your iOS developer portfolio is now ready for deployment! 🚀** 