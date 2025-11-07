# LiveKit Voice Agent Mobile App

A React Native mobile application for interacting with LiveKit Voice Agents.

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

## Features

- 🎤 Real-time voice conversations with AI agents
- 📱 Cross-platform support (iOS & Android)
- 🔊 Audio session management
- 🎯 Multiple agent personalities
- 💬 Text-based chat fallback
- 🔐 User authentication
- 📊 Conversation history
- 🔔 Push notifications

## Tech Stack

- **Framework**: React Native 0.73+
- **LiveKit**: @livekit/react-native
- **WebRTC**: @livekit/react-native-webrtc
- **Navigation**: React Navigation 6
- **State Management**: Zustand
- **UI Components**: React Native Elements / NativeBase
- **Audio**: React Native Audio Session
- **Authentication**: Firebase Auth / Supabase Auth

## Project Structure

```
mobile/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── AudioControls/
│   │   ├── ChatInterface/
│   │   ├── AgentSelector/
│   │   └── SettingsPanel/
│   ├── screens/             # Screen components
│   │   ├── HomeScreen.tsx
│   │   ├── CallScreen.tsx
│   │   ├── HistoryScreen.tsx
│   │   └── SettingsScreen.tsx
│   ├── services/            # Business logic
│   │   ├── livekit.ts       # LiveKit client
│   │   ├── auth.ts          # Authentication
│   │   └── storage.ts       # Local storage
│   ├── hooks/               # Custom React hooks
│   │   ├── useAudioSession.ts
│   │   ├── useLiveKit.ts
│   │   └── useAuth.ts
│   ├── store/               # State management
│   │   └── index.ts
│   ├── types/               # TypeScript definitions
│   │   └── index.ts
│   └── utils/               # Utility functions
│       └── helpers.ts
├── android/                 # Android-specific code
├── ios/                     # iOS-specific code
├── __tests__/               # Test files
└── docs/                    # Documentation
```

## Getting Started

### Prerequisites

- Node.js 18+
- React Native development environment
- iOS: Xcode 14+
- Android: Android Studio

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. iOS setup:
   ```bash
   cd ios && pod install && cd ..
   ```

4. Start the development server:
   ```bash
   # For Android
   npm run android
   
   # For iOS
   npm run ios
   ```

## Configuration

Create a `.env` file in the root directory:

```env
LIVEKIT_SERVER_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret

# Authentication (optional)
FIREBASE_API_KEY=your-firebase-api-key
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-anon-key
```

## Usage

1. **Connecting to an Agent**: Select an agent from the home screen and tap "Start Call"
2. **Voice Conversation**: Use the audio controls to mute/unmute and manage the call
3. **Text Chat**: Switch to text mode for typing-based interaction
4. **History**: View past conversations in the History screen
5. **Settings**: Configure audio preferences and agent options

## Development

### Running Tests

```bash
npm test
```

### Building for Production

```bash
# Android
npm run build:android

# iOS
npm run build:ios
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details
