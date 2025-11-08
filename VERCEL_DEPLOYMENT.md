# Security+ Agent - Vercel Deployment Guide

## 🚀 Deploy to Vercel

This guide will help you deploy the Security+ Exam Teaching Assistant web interface to Vercel.

### Prerequisites

1. **LiveKit Server** - Running LiveKit server for real-time audio
2. **Security+ Agent Backend** - Python backend with the Security+ teaching agent
3. **Vercel Account** - Free Vercel account for deployment

### Environment Variables

Configure these environment variables in Vercel:

```
LIVEKIT_HOST=your-livekit-server.com
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

### Deployment Steps

#### 1. Install Dependencies
```bash
npm install
```

#### 2. Deploy to Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy to Vercel
vercel --prod
```

#### 3. Configure Environment Variables in Vercel Dashboard
1. Go to your Vercel project dashboard
2. Navigate to **Settings → Environment Variables**
3. Add the required environment variables:
   - `LIVEKIT_HOST` - Your LiveKit server URL
   - `LIVEKIT_API_KEY` - Your LiveKit API key
   - `LIVEKIT_API_SECRET` - Your LiveKit API secret

#### 4. Redeploy with Environment Variables
```bash
vercel --prod
```

### Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────────┐
│   Vercel    │────▶│ LiveKit     │────▶│ Security+       │
│ (Frontend)  │     │ Server      │     │ Agent Backend  │
│             │     │             │     │ (Python)        │
│ - UI/UX     │     │ - Audio     │     │ - AI Teaching   │
│ - Token API │     │   Streaming │     │ - Security+     │
│ - WebRTC    │     │ - Room Mgmt │     │   Content       │
└─────────────┘     └─────────────┘     └─────────────────┘
```

### Features

- **Real-time Voice Communication** - LiveKit WebRTC audio streaming
- **Security+ Exam Content** - Comprehensive exam preparation material
- **Interactive Learning** - AI-powered teaching assistant
- **Token-based Authentication** - Secure room access via Vercel API
- **Responsive Design** - Works on desktop and mobile devices

### Local Development

#### 1. Start the Security+ Backend
```bash
cd /path/to/your/project
source .venv/bin/activate
uv run python security_plus_agent.py start
```

#### 2. Start the Frontend
```bash
npm run dev
```

#### 3. Access the Application
Open `http://localhost:3000` in your browser.

### Configuration

#### LiveKit Server Setup
1. Install LiveKit server
2. Configure with your API keys
3. Update environment variables

#### Security+ Agent Backend
1. Configure OpenAI API key in `.env`
2. Set up Security+ knowledge base
3. Start the agent server

### Troubleshooting

#### Common Issues

1. **Connection Failed**
   - Check LiveKit server URL
   - Verify API keys in environment variables
   - Ensure backend is running

2. **Audio Not Working**
   - Check browser microphone permissions
   - Verify WebRTC configuration
   - Check network connectivity

3. **Token Generation Error**
   - Verify LiveKit API credentials
   - Check Vercel environment variables
   - Review API route logs

#### Debug Mode

Enable debug logging:
```bash
DEBUG=* npm run dev
```

### Production Considerations

- **SSL Certificate** - Required for WebRTC
- **CORS Configuration** - Allow your Vercel domain
- **Rate Limiting** - Implement on token endpoint
- **Monitoring** - Set up error tracking

### Support

For issues with:
- **Vercel Deployment** - Check Vercel documentation
- **LiveKit Integration** - Review LiveKit docs
- **Security+ Agent** - Check agent logs and configuration

---

**Note**: This deployment includes only the web frontend. The Security+ Python agent backend needs to be deployed separately (e.g., on Heroku, Railway, or a cloud VM).
