# Quick Start Guide

Get your LiveKit Voice Agent mobile app running in minutes!

## 🚀 One-Command Setup

```bash
# Clone and setup everything
cd mobile
npm run setup
```

## 📱 Run the App

### iOS (macOS only)
```bash
npm run ios
```

### Android
```bash
npm run android
```

## ⚙️ Configuration

1. **Copy environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your LiveKit server:**
   ```env
   LIVEKIT_SERVER_URL=wss://your-livekit-server.com
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   ```

3. **Start your backend agent:**
   ```bash
   # From the parent directory
   uv run python livekit_basic_agent.py start
   ```

## 🎯 Test the Connection

1. Open the mobile app
2. Select an agent (e.g., "General Assistant")
3. Tap "Start Call"
4. Grant microphone permissions
5. Start talking!

## 🔧 Troubleshooting

### Build Issues
```bash
# Clear everything and restart
npm run clean
npm run setup
```

### iOS Issues
```bash
# Reinstall pods
cd ios && pod install && cd ..
```

### Android Issues
```bash
# Clean Android build
cd android && ./gradlew clean && cd ..
```

### Connection Issues
- Verify your LiveKit server is running
- Check the server URL in `.env`
- Ensure API keys are correct

## 📚 Next Steps

- Read [SETUP.md](./SETUP.md) for detailed setup
- Read [MOBILE_INTEGRATION.md](../MOBILE_INTEGRATION.md) for backend integration
- Check the main [README.md](./README.md) for all features

## 🆘 Need Help?

- Check the troubleshooting section in SETUP.md
- Review the integration guide
- Open an issue on GitHub
