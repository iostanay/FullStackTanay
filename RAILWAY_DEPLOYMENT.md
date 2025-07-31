# Railway Deployment Guide

This guide will help you deploy your iOS Developer Portfolio to Railway.

## Prerequisites

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login to Railway:
   ```bash
   railway login
   ```

## Deployment Steps

### 1. Initialize Railway Project

Navigate to your project directory and run:
```bash
railway init
```

### 2. Link to Railway Project

If you haven't created a project yet:
```bash
railway link
```

### 3. Deploy to Railway

Deploy your application:
```bash
railway up
```

### 4. Set Environment Variables (Optional)

If you need to set environment variables:
```bash
railway variables set VARIABLE_NAME=value
```

### 5. Get Your Deployment URL

View your deployment:
```bash
railway status
```

## Configuration Files

The following files have been created for Railway deployment:

- `railway.json`: Railway-specific configuration
- `Procfile`: Specifies how to run the application
- `runtime.txt`: Specifies Python version
- `.railwayignore`: Excludes unnecessary files from deployment

## Environment Variables

The application is configured to use the following environment variables:

- `PORT`: Railway will automatically set this (defaults to 8000)

## Monitoring

- View logs: `railway logs`
- Monitor deployment: `railway status`
- Open in browser: `railway open`

## Troubleshooting

1. **Build fails**: Check that all dependencies are in `requirements.txt`
2. **App doesn't start**: Check the logs with `railway logs`
3. **Port issues**: The app is configured to use Railway's PORT environment variable

## Custom Domain (Optional)

To add a custom domain:
1. Go to your Railway dashboard
2. Select your project
3. Go to Settings > Domains
4. Add your custom domain

## SSL Certificate

Railway automatically provides SSL certificates for your deployments. 