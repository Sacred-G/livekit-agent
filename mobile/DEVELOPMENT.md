# Development Guide

This guide covers development setup and troubleshooting for the LiveKit Voice Agent mobile app.

## 🛠️ Development Setup

### Prerequisites
- Node.js 18+
- React Native CLI
- Xcode 14+ (iOS)
- Android Studio (Android)

### Initial Setup

```bash
# Clone and navigate to mobile directory
cd mobile

# Run the automated setup script
./install.sh

# Or manual setup
npm run setup
```

## 🔍 Lint and Type Checking

### Before Dependencies Are Installed

Since TypeScript and ESLint require dependencies to be installed for full type checking, we provide development-friendly configurations:

```bash
# Development linting (ignores missing dependencies)
npm run lint:dev

# Development type checking (skips lib checks)
npm run type-check:dev
```

### After Dependencies Are Installed

Once you run `npm install`, you can use the stricter configurations:

```bash
# Full linting with all rules
npm run lint

# Full type checking
npm run type-check
```

## 🐛 Common Development Issues

### TypeScript Errors Before Installation

**Issue**: "Cannot find module 'react'" or similar errors
**Solution**: These are expected before running `npm install`. Use `npm run type-check:dev` for development checking.

### ESLint Configuration Issues

**Issue**: Import resolution errors
**Solution**: The development ESLint config (`.eslintrc.dev.js`) handles missing dependencies gracefully.

### Metro Bundler Issues

```bash
# Clear Metro cache
npx react-native start --reset-cache

# Clear node_modules and reinstall
rm -rf node_modules && npm install
```

### iOS Build Issues

```bash
# Clean iOS build
cd ios && xcodebuild clean && cd ..

# Reinstall pods
cd ios && rm -rf Pods && pod install && cd ..
```

### Android Build Issues

```bash
# Clean Android build
cd android && ./gradlew clean && cd ..

# Reset Android project
cd android && ./gradlew cleanBuildCache && cd ..
```

## 🧪 Testing

### Unit Tests
```bash
npm test
```

### E2E Testing
```bash
# If you have E2E tests configured
npm run test:e2e
```

### Manual Testing Checklist

1. **App Launch**: App starts without crashes
2. **Agent Selection**: Can select and view agents
3. **Voice Call**: Can initiate and maintain voice calls
4. **Audio Controls**: Mute/unmute and volume controls work
5. **Navigation**: All screens navigate properly
6. **Settings**: Preferences persist correctly

## 🔧 Development Workflow

### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes

# Development linting
npm run lint:dev

# Development type checking
npm run type-check:dev
```

### 2. Testing
```bash
# Start Metro bundler
npm start

# Run on iOS simulator
npm run ios

# Run on Android emulator
npm run android
```

### 3. Pre-commit Checks
```bash
# Full linting (after dependencies installed)
npm run lint

# Full type checking
npm run type-check

# Run tests
npm test
```

## 📱 Platform-Specific Development

### iOS Development
- Use Xcode for debugging and profiling
- Test on multiple iOS versions
- Check background audio permissions
- Verify push notification setup

### Android Development
- Use Android Studio for debugging
- Test on different API levels
- Check runtime permissions
- Verify background service configuration

## 🚨 Debugging

### Console Logs
The app includes console logging for debugging:
```javascript
console.log('Debug info:', data);
```

### React Native Debugger
```bash
# Install React Native Debugger
# Then start your app and connect to the debugger
```

### Flipper (iOS)
Flipper is included in the debug build for iOS development.

## 📝 Code Style

### TypeScript
- Use interfaces for type definitions
- Prefer explicit types over `any`
- Use proper async/await patterns

### React Native
- Follow React Native naming conventions
- Use functional components with hooks
- Implement proper cleanup in useEffect

### File Organization
```
src/
├── components/     # Reusable UI components
├── screens/        # Screen components
├── services/       # Business logic and API calls
├── hooks/          # Custom React hooks
├── store/          # State management
├── types/          # TypeScript definitions
└── utils/          # Utility functions
```

## 🔐 Environment Variables

Create a `.env` file for development:
```env
LIVEKIT_SERVER_URL=wss://localhost:7880
DEBUG_MODE=true
LOG_LEVEL=debug
```

## 📚 Additional Resources

- [React Native Documentation](https://reactnative.dev/)
- [LiveKit React Native SDK](https://github.com/livekit/client-sdk-react-native)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Navigation](https://reactnavigation.org/)

## 🆘 Getting Help

1. Check this development guide
2. Review the main README.md
3. Look at the troubleshooting section in SETUP.md
4. Open an issue on GitHub with detailed error information
