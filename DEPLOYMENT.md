# Deployment Guide for Render

This guide will help you deploy ONEDeFi Server to Render.

## Prerequisites

1. A GitHub account with this repository
2. A Render account (free tier works)
3. Your OpenAI API key (for AI features)

## Step-by-Step Deployment

### 1. Push to GitHub

Make sure your code is pushed to a GitHub repository:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Connect your GitHub repository

### 3. Create Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `onedefi-server` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120`
   - **Plan**: Free (or choose a paid plan for better performance)

### 4. Create PostgreSQL Database

1. Click "New +" → "PostgreSQL"
2. Configure:
   - **Name**: `onedefi-db`
   - **Database**: `onedefi`
   - **User**: `onedefi_user`
   - **Plan**: Free (or choose a paid plan)

### 5. Configure Environment Variables

In your Web Service settings, add these environment variables:

- `DATABASE_URL`: (Auto-populated if you link the database)
- `SESSION_SECRET`: Generate a random secret key (e.g., use `openssl rand -hex 32`)
- `FLASK_ENV`: `production`
- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: (Auto-set by Render, don't override)

### 6. Deploy

1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Wait for the build to complete (usually 5-10 minutes)
4. Your app will be available at `https://your-app-name.onrender.com`

## Post-Deployment

### Verify Deployment

1. Visit your Render URL
2. Check that the homepage loads correctly
3. Test the API endpoints
4. Verify database connection

### Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain and follow DNS configuration instructions

## Troubleshooting

### Build Fails

- Check build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Database Connection Issues

- Ensure `DATABASE_URL` is set correctly
- Check that the database is linked to your web service
- Verify PostgreSQL connection string format

### Application Errors

- Check application logs in Render dashboard
- Verify all environment variables are set
- Ensure `FLASK_ENV=production` is set

## Performance Optimization

For better performance on Render:

1. **Upgrade Plan**: Use a paid plan for better resources
2. **Database**: Use a paid PostgreSQL plan for better performance
3. **Workers**: Adjust Gunicorn workers based on your plan:
   - Free: 1-2 workers
   - Starter: 2-4 workers
   - Professional: 4+ workers

## Monitoring

Render provides:
- Application logs
- Metrics dashboard
- Automatic SSL certificates
- Health checks

## Support

For issues:
1. Check Render documentation: https://render.com/docs
2. Review application logs
3. Check Flask/Gunicorn documentation

---

**Note**: The free tier on Render may spin down after inactivity. Consider upgrading for production use.

