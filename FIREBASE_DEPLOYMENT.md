# Firebase Hosting + Cloud Functions Deployment Guide

This guide will help you deploy your iOS Developer Portfolio to Firebase Hosting using Cloud Functions.

## 🚀 Quick Start

### 1. Install Firebase CLI
```bash
# Install Node.js first (if not installed)
# Download from: https://nodejs.org/

# Install Firebase CLI
npm install -g firebase-tools
```

### 2. Login to Firebase
```bash
firebase login
```

### 3. Initialize Firebase Project
```bash
firebase init
```

Select:
- ✅ Hosting
- ✅ Functions
- Choose project: `tanayios-ai` (or create new)
- Use existing project: `tanayios-ai`
- Public directory: `public`
- Single-page app: `No`
- Overwrite index.html: `No`

### 4. Deploy to Firebase
```bash
firebase deploy
```

## 📁 Project Structure

```
ios-developer-portfolio/
├── firebase.json          # Firebase configuration
├── functions/
│   ├── main.py           # Cloud Function (Flask app)
│   ├── requirements.txt  # Python dependencies
│   └── .firebaserc      # Project config
├── public/
│   └── index.html        # Loading page
├── app.py               # Your Flask app
├── templates/           # Flask templates
└── static/             # Static files
```

## 🔧 Configuration Files

### firebase.json
- Configures hosting and functions
- Routes all requests to Cloud Function
- Uses Python 3.11 runtime

### functions/main.py
- Cloud Function that serves your Flask app
- Handles WSGI environment conversion
- Integrates with Firebase Admin SDK

### functions/requirements.txt
- Python dependencies for Cloud Functions
- Includes Firebase Functions SDK

## 🌐 Custom Domain Setup

### 1. Add Custom Domain
```bash
firebase hosting:sites:add tanayios-ai
```

### 2. Configure DNS
- Go to Firebase Console > Hosting
- Add custom domain: `tanayios-ai.web.app`
- Follow DNS configuration instructions

### 3. Verify Domain
```bash
firebase hosting:channel:deploy preview
```

## 📊 Monitoring & Analytics

### View Logs
```bash
firebase functions:log
```

### Monitor Performance
- Firebase Console > Functions
- View execution times and errors

## 🔄 Deployment Commands

### Deploy Everything
```bash
firebase deploy
```

### Deploy Only Functions
```bash
firebase deploy --only functions
```

### Deploy Only Hosting
```bash
firebase deploy --only hosting
```

### Deploy to Preview Channel
```bash
firebase hosting:channel:deploy preview
```

## 🛠️ Troubleshooting

### Common Issues

1. **Function Timeout**
   - Increase timeout in firebase.json
   - Optimize Flask app performance

2. **Memory Issues**
   - Check function memory usage
   - Optimize static file serving

3. **Cold Start**
   - Use Firebase Hosting for static files
   - Implement caching strategies

### Debug Commands
```bash
# Test functions locally
firebase emulators:start

# View function logs
firebase functions:log

# Check deployment status
firebase projects:list
```

## 💰 Pricing

- **Hosting**: Free tier includes 10GB storage, 360MB/day transfer
- **Functions**: Free tier includes 2M invocations/month
- **Custom Domain**: Free SSL certificates

## 🎯 Benefits of Firebase

✅ **Global CDN** - Fast loading worldwide  
✅ **Automatic SSL** - Secure HTTPS by default  
✅ **Custom Domains** - Use your own domain  
✅ **Serverless** - No server management  
✅ **Scalable** - Handles traffic spikes  
✅ **Free Tier** - Generous free limits  

## 🚀 Your App URL

After deployment, your app will be available at:
- **Firebase URL**: `https://tanayios-ai.web.app`
- **Custom Domain**: `https://tanayios-ai.web.app` (if configured)

## 📱 iOS Developer Portfolio Features

Your portfolio includes:
- ✅ Responsive design
- ✅ iOS development showcase
- ✅ Project highlights
- ✅ Skills and experience
- ✅ Contact information
- ✅ Modern UI/UX

Ready to deploy! 🚀 