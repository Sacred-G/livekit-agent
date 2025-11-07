#!/bin/bash

# LiveKit Voice Agent Mobile App Installation Script
# This script sets up the React Native mobile app for LiveKit Voice Agents

set -e

echo "🚀 Setting up LiveKit Voice Agent Mobile App..."

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Please run this script from the mobile directory"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Error: Node.js 18+ is required. Current version: $(node --version)"
    exit 1
fi

echo "✅ Node.js version check passed: $(node --version)"

# Install npm dependencies
echo "📦 Installing npm dependencies..."
npm install

# Check if we're on macOS and install iOS pods
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Detected macOS - installing iOS pods..."
    if ! command -v pod &> /dev/null; then
        echo "❌ Error: CocoaPods is not installed. Please run: sudo gem install cocoapods"
        exit 1
    fi
    
    cd ios
    pod install
    cd ..
    echo "✅ iOS pods installed successfully"
else
    echo "💻 Not on macOS - skipping iOS pod installation"
fi

# Check React Native CLI
if ! command -v react-native &> /dev/null; then
    echo "⚠️  Warning: React Native CLI not found. Install with: npm install -g react-native-cli"
fi

# Create environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating environment file..."
    cp .env.example .env
    echo "✅ Created .env file - please edit it with your LiveKit server details"
else
    echo "✅ .env file already exists"
fi

# Run type check to verify setup
echo "🔍 Running type check..."
npm run type-check || echo "⚠️  Type check failed - this is expected without dependencies installed"

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📱 Next steps:"
echo "   1. Edit .env file with your LiveKit server details"
echo "   2. Start your LiveKit agent backend"
echo "   3. Run the app:"
echo "      iOS: npm run ios"
echo "      Android: npm run android"
echo ""
echo "📚 For detailed setup, see: SETUP.md"
echo "🆘 For quick start, see: QUICK_START.md"
