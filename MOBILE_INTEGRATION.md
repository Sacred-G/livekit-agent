# Mobile App Integration Guide

This guide explains how to integrate the React Native mobile app with your LiveKit Voice Agent backend.

## Overview

The mobile app provides a native iOS/Android interface for users to interact with your LiveKit Voice Agents. It includes:

- 🎤 Real-time voice conversations
- 📱 Cross-platform support (iOS & Android)
- 🎯 Multiple agent selection
- 💬 Text-based chat fallback
- 📊 Conversation history
- 🔔 Push notifications
- 🔐 User authentication

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React Native  │───▶│  LiveKit Server  │───▶│  Voice Agent    │
│   Mobile App    │    │   (Cloud/Local)  │    │   (Python)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
    ┌────▼────┐            ┌─────▼──────┐         ┌─────▼──────┐
    │   UI    │            │   Audio    │         │   Tools    │
    │ Layer   │            │ Streaming  │         │ (MCP)      │
    └─────────┘            └────────────┘         └────────────┘
```

## Quick Start

### 1. Backend Setup

Ensure your LiveKit Voice Agent is running and accessible:

```bash
# Start your agent (example with basic agent)
uv run python livekit_basic_agent.py start

# Or start with MCP agent
uv run python livekit_mcp_agent.py start
```

### 2. Mobile App Setup

```bash
# Navigate to mobile directory
cd mobile

# Install dependencies
npm install

# iOS setup (if on macOS)
cd ios && pod install && cd ..

# Configure environment
cp .env.example .env
# Edit .env with your server details
```

### 3. Configure Connection

Edit `.env` in the mobile directory:

```env
LIVEKIT_SERVER_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
```

### 4. Run the App

```bash
# Start Metro bundler
npm start

# Run on iOS
npm run ios

# Run on Android
npm run android
```

## Token Generation

The mobile app requires JWT tokens to connect to LiveKit rooms. You need to implement a token generation endpoint in your backend.

### Backend Token Service Example

Create a new file `token_service.py`:

```python
from livekit import api
import os
from datetime import datetime, timedelta

class TokenService:
    def __init__(self):
        self.livekit_host = os.getenv("LIVEKIT_URL")
        self.api_key = os.getenv("LIVEKIT_API_KEY")
        self.api_secret = os.getenv("LIVEKIT_API_SECRET")
    
    def generate_token(self, room_name: str, participant_name: str) -> str:
        """Generate a LiveKit token for mobile client"""
        
        token = api.AccessToken(
            api_key=self.api_key,
            api_secret=self.api_secret,
            identity=participant_name,
            name=participant_name
        )
        
        token.add_grant(api.VideoGrant(
            room_join=True,
            room=room_name,
            can_publish=True,
            can_subscribe=True
        ))
        
        # Set token to expire in 2 hours
        expiration = datetime.utcnow() + timedelta(hours=2)
        token.identity = participant_name
        token.name = participant_name
        
        return token.to_jwt(expiration=expiration)

# Usage
token_service = TokenService()
token = token_service.generate_token("room_123", "mobile_user")
print(token)
```

### API Endpoint for Mobile App

Add to your existing agent or create a FastAPI endpoint:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class TokenRequest(BaseModel):
    agent_id: str
    user_id: str = None

class TokenResponse(BaseModel):
    token: str
    room_name: str
    server_url: str

@app.post("/api/token", response_model=TokenResponse)
async def get_token(request: TokenRequest):
    try:
        # Generate unique room name
        room_name = f"room_{uuid.uuid4().hex[:8]}"
        participant_name = request.user_id or f"user_{uuid.uuid4().hex[:8]}"
        
        # Generate token
        token = token_service.generate_token(room_name, participant_name)
        
        return TokenResponse(
            token=token,
            room_name=room_name,
            server_url=os.getenv("LIVEKIT_URL")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Authentication Integration

### Option 1: Firebase Authentication

1. **Set up Firebase project**
2. **Add Firebase SDK to mobile app** (already in package.json)
3. **Configure Firebase in mobile app**:

```javascript
// src/services/auth.ts
import auth from '@react-native-firebase/auth';

export const signIn = async (email: string, password: string) => {
  try {
    const userCredential = await auth().signInWithEmailAndPassword(email, password);
    return userCredential.user;
  } catch (error) {
    throw error;
  }
};

export const signOut = async () => {
  try {
    await auth().signOut();
  } catch (error) {
    throw error;
  }
};
```

### Option 2: Custom Authentication

Implement your own auth system and integrate with the mobile app:

```javascript
// src/services/auth.ts
export const customSignIn = async (credentials: any) => {
  const response = await fetch('https://your-api.com/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(credentials),
  });
  
  const data = await response.json();
  return data.user;
};
```

## Push Notifications

### Firebase Cloud Messaging Setup

1. **Enable FCM in Firebase project**
2. **Configure iOS/Android**:
   - iOS: Upload APNs certificate
   - Android: Add server key

3. **Handle notifications in mobile app**:

```javascript
// src/services/notifications.ts
import messaging from '@react-native-firebase/messaging';

export const requestNotificationPermission = async () => {
  const authStatus = await messaging().requestPermission();
  return (
    authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
    authStatus === messaging.AuthorizationStatus.PROVISIONAL
  );
};

export const getFCMToken = async () => {
  return await messaging().getToken();
};

// Handle background messages
messaging().setBackgroundMessageHandler(async remoteMessage => {
  console.log('Message handled in the background!', remoteMessage);
});
```

## Agent Configuration

### Available Agents

Configure your agents in the mobile app:

```javascript
// src/config/agents.ts
export const AGENTS = [
  {
    id: 'assistant',
    name: 'General Assistant',
    description: 'Helpful AI assistant for everyday tasks',
    capabilities: ['conversation', 'information', 'tasks'],
    status: 'online'
  },
  {
    id: 'security',
    name: 'Security Expert',
    description: 'Specialized in cybersecurity and best practices',
    capabilities: ['security', 'analysis', 'guidance'],
    status: 'online'
  },
  // Add your custom agents here
];
```

### Custom Agent Integration

To add your custom agents:

1. **Define agent configuration** in the mobile app
2. **Ensure agent is running** in your backend
3. **Test connection** with the mobile app

## Deployment

### Building for Production

#### iOS
```bash
cd ios
xcodebuild -workspace LiveKitVoiceAgent.xcworkspace \
           -scheme LiveKitVoiceAgent \
           -configuration Release \
           -destination generic/platform=iOS \
           -archivePath LiveKitVoiceAgent.xcarchive archive
```

#### Android
```bash
cd android
./gradlew assembleRelease
```

### App Store Distribution

1. **Build archive** using Xcode
2. **Upload to App Store Connect**
3. **Configure app metadata**
4. **Submit for review**

### Google Play Distribution

1. **Build signed APK/AAB**
2. **Upload to Google Play Console**
3. **Complete store listing**
4. **Submit for review**

## Testing

### Unit Tests
```bash
npm test
```

### Integration Tests
Test the connection between mobile app and backend:

```javascript
// __tests__/integration.test.js
import { LiveKitService } from '../src/services/livekit';

describe('LiveKit Integration', () => {
  test('should connect to agent', async () => {
    const service = LiveKitService.getInstance();
    const agent = { id: 'assistant', name: 'Test Agent' };
    
    const room = await service.connectToAgent(
      agent, 
      'wss://test-server.com', 
      'test-token'
    );
    
    expect(room).toBeDefined();
    expect(room.agentId).toBe(agent.id);
  });
});
```

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check LiveKit server URL
   - Verify API keys
   - Test network connectivity

2. **Audio Issues**
   - Check microphone permissions
   - Verify audio session setup
   - Test with different audio devices

3. **Token Generation Errors**
   - Verify API key/secret
   - Check token expiration
   - Validate room permissions

4. **Build Issues**
   - Clear caches: `npm start -- --reset-cache`
   - Reinstall dependencies: `rm -rf node_modules && npm install`
   - Update pods: `cd ios && pod install`

### Debug Mode

Enable debug logging:
```env
DEBUG_MODE=true
LOG_LEVEL=debug
```

## Security Considerations

1. **Token Security**: Never expose API secrets in mobile app
2. **Network Security**: Use HTTPS for all API calls
3. **Authentication**: Implement proper user authentication
4. **Data Storage**: Encrypt sensitive data locally
5. **Permissions**: Request only necessary permissions

## Performance Optimization

1. **Audio Quality**: Adjust based on network conditions
2. **Battery Usage**: Optimize background processing
3. **Memory Management**: Proper cleanup of audio sessions
4. **Network**: Implement reconnection logic

## Next Steps

1. **Custom UI**: Design branded interface
2. **Advanced Features**: Add screen sharing, file transfer
3. **Analytics**: Implement usage tracking
4. **Multi-language**: Add internationalization
5. **Offline Mode**: Cache conversations locally

## Support

- **Documentation**: Check `mobile/README.md`
- **Issues**: Report bugs in GitHub repository
- **Community**: Join our Discord for support
- **LiveKit Docs**: https://docs.livekit.io/
