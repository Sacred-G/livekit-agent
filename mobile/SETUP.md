# LiveKit Voice Agent Mobile App - Setup Guide

This guide will help you set up the React Native mobile app for LiveKit Voice Agents.

## Prerequisites

### Required Software
- **Node.js** 18+ 
- **React Native CLI**: `npm install -g react-native-cli`
- **Watchman** (macOS): `brew install watchman`
- **CocoaPods** (macOS): `sudo gem install cocoapods`

### Platform Requirements
- **iOS**: Xcode 14+ and iOS 12+ target
- **Android**: Android Studio, Android SDK 33+, Java 11+

## Installation Steps

### 1. Clone and Navigate
```bash
cd /path/to/livekit-agent/mobile
```

### 2. Install Dependencies
```bash
# Using npm
npm install

# Using yarn
yarn install
```

### 3. iOS Setup
```bash
cd ios
pod install
cd ..
```

### 4. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

Required environment variables:
```env
LIVEKIT_SERVER_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
```

## Platform-Specific Setup

### iOS Configuration

#### 1. Audio Session Setup
Add to `ios/LiveKitVoiceAgent/AppDelegate.mm`:

```objc
#import "LivekitReactNative.h"
#import "WebRTCModuleOptions.h"

@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Place this above any other RN related initialization
    [LivekitReactNative setup];
    
    // Uncomment for background camera access (iOS 18+)
    // WebRTCModuleOptions *options = [WebRTCModuleOptions sharedInstance];
    // options.enableMultitaskingCameraAccess = YES;
    
    return YES;
}
@end
```

#### 2. Permissions
Add to `ios/LiveKitVoiceAgent/Info.plist`:

```xml
<key>NSMicrophoneUsageDescription</key>
<string>This app needs microphone access for voice conversations with AI agents</string>
<key>NSCameraUsageDescription</key>
<string>This app needs camera access for video calls with AI agents</string>
```

#### 3. Background Modes
Add to `ios/LiveKitVoiceAgent/Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
    <string>audio</string>
    <string>voip</string>
</array>
```

### Android Configuration

#### 1. MainApplication Setup
Add to `android/app/src/main/java/com/livekitvoiceagent/MainApplication.java`:

```java
import com.livekit.reactnative.LiveKitReactNative;
import com.livekit.reactnative.audio.AudioType;

public class MainApplication extends Application implements ReactApplication {
    @Override
    public void onCreate() {
        // Place this above any other RN related initialization
        LiveKitReactNative.setup(this, new AudioType.CommunicationAudioType());
        
        super.onCreate();
    }
}
```

#### 2. Permissions
Add to `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

#### 3. ProGuard Rules
Add to `android/app/proguard-rules.pro`:

```proguard
-keep class org.webrtc.** { *; }
-keep class com.livekit.reactnative.** { *; }
```

## Running the App

### Development Mode

#### iOS
```bash
# Start Metro bundler
npm start

# Run on iOS simulator
npm run ios

# Or run on specific device
npm run ios -- --simulator="iPhone 14"
```

#### Android
```bash
# Start Metro bundler
npm start

# Run on Android emulator/device
npm run android
```

### Production Build

#### iOS
```bash
# Build for iOS
cd ios
xcodebuild -workspace LiveKitVoiceAgent.xcworkspace \
           -scheme LiveKitVoiceAgent \
           -configuration Release \
           -destination generic/platform=iOS \
           -archivePath LiveKitVoiceAgent.xcarchive archive
```

#### Android
```bash
# Build APK
npm run build:android

# Build AAB for Play Store
cd android
./gradlew bundleRelease
```

## Troubleshooting

### Common Issues

#### 1. Metro bundler issues
```bash
# Clear Metro cache
npx react-native start --reset-cache

# Clear node_modules
rm -rf node_modules && npm install
```

#### 2. iOS build issues
```bash
# Clear iOS build cache
cd ios && xcodebuild clean && cd ..

# Reinstall pods
cd ios && rm -rf Pods && pod install && cd ..
```

#### 3. Android build issues
```bash
# Clean Android build
cd android && ./gradlew clean && cd ..

# Reset Android project
cd android && ./gradlew cleanBuildCache && cd ..
```

#### 4. LiveKit connection issues
- Verify server URL is accessible
- Check API keys are correct
- Ensure network permissions are granted
- Test with LiveKit Cloud for debugging

### Debug Mode

Enable debug logging by setting:
```env
DEBUG_MODE=true
LOG_LEVEL=debug
```

### Testing

#### Unit Tests
```bash
npm test
```

#### E2E Tests (if configured)
```bash
npm run test:e2e
```

## Deployment

### App Store (iOS)
1. Build archive using Xcode
2. Upload to App Store Connect
3. Complete App Store review process

### Google Play (Android)
1. Build signed AAB
2. Upload to Google Play Console
3. Complete review process

### Firebase App Distribution (Alternative)
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Deploy to Firebase App Distribution
firebase appdistribution:distribute \
  --app <your-firebase-app-id> \
  --release-notes "New version with LiveKit integration" \
  --groups "testers"
```

## Next Steps

1. **Configure Backend**: Set up your LiveKit server and token generation
2. **Add Authentication**: Implement Firebase/Supabase authentication
3. **Push Notifications**: Configure Firebase Cloud Messaging
4. **Analytics**: Add crash reporting and analytics
5. **Testing**: Write comprehensive tests
6. **CI/CD**: Set up automated builds and deployments

## Support

- **LiveKit Documentation**: https://docs.livekit.io/
- **React Native Docs**: https://reactnative.dev/
- **GitHub Issues**: Report bugs in the repository
- **Community**: Join our Discord community for support
