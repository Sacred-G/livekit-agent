#!/bin/bash

# LiveKit Security+ Agent - One Click Start (Linux)
# ================================================

echo "🚀 Starting LiveKit Security+ Agent..."

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV not found. Please install UV first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "   source ~/.bashrc"
    read -p "Press Enter to exit..."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    read -p "Press Enter to exit..."
    exit 1
fi

# Start local LiveKit server
echo "🔧 Starting LiveKit server..."
if [ ! -f "keys.txt" ]; then
    echo "APIJzcLNvtmYEiU: 7MfPzoCaV7LeSt05ZpYf6XD7G5TUfqb1WSFZxMpKGAKD" > keys.txt
    chmod 600 keys.txt
fi

livekit-server --dev --key-file keys.txt > /tmp/livekit-server.log 2>&1 &
SERVER_PID=$!
sleep 3

# Start vision agent
echo "🤖 Starting Security+ Vision Agent..."
uv run python vision_agent.py connect --room security-plus-room --url ws://localhost:7880 --api-key APIJzcLNvtmYEiU --api-secret "7MfPzoCaV7LeSt05ZpYf6XD7G5TUfqb1WSFZxMpKGAKD" > /tmp/agent.log 2>&1 &
AGENT_PID=$!
sleep 3

# Start frontend
echo "🌐 Starting Frontend..."
cd frontend
npm run dev > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!
sleep 2

# Success message
echo ""
echo "✅ All services started successfully!"
echo "=================================="
echo "🌐 Frontend: http://localhost:3000"
echo "🎓 Agent: Security+ Vision Teacher"
echo "👁️ Vision: ENABLED (can see your screen)"
echo "🔊 Audio: ENABLED"
echo ""
echo "📋 Available commands:"
echo "   • 'Quiz me' - Practice questions"
echo "   • 'Teach me about [topic]' - Start lesson"
echo "   • 'Can you see my screen?' - Test vision"
echo "   • 'Analyze my screen' - Screen analysis"
echo ""
echo "📝 Logs:"
echo "   • Server: /tmp/livekit-server.log"
echo "   • Agent: /tmp/agent.log"
echo "   • Frontend: /tmp/frontend.log"
echo ""
echo "Press Ctrl+C to stop all services"

# Cleanup function
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $AGENT_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    kill $SERVER_PID 2>/dev/null
    echo "✅ All services stopped"
    exit 0
}

# Set trap for cleanup
trap cleanup INT

# Wait for processes
wait
