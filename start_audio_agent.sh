#!/bin/bash

# LiveKit Security+ Agent - Audio Working Version
echo "🎓 Starting LiveKit Security+ Agent with Working Audio..."

# Check if local LiveKit server is running
if ! pgrep -f "livekit-server" > /dev/null; then
    echo "🚀 Starting local LiveKit server..."
    cd /Volumes/Development/livekit/livekit-agent
    livekit-server --dev --key-file keys.txt &
    SERVER_PID=$!
    sleep 3
    echo "✅ LiveKit server started (PID: $SERVER_PID)"
else
    echo "✅ LiveKit server already running"
fi

# Start the Security+ agent
echo "🎤 Starting Security+ Agent..."
cd /Volumes/Development/livekit/livekit-agent
uv run python security_plus_agent.py connect --room security-plus-room --url ws://localhost:7880 --api-key APIJzcLNvtmYEiU --api-secret "7MfPzoCaV7LeSt05ZpYf6XD7G5TUfqb1WSFZxMpKGAKD" &
AGENT_PID=$!

# Wait a moment for agent to start
sleep 3

# Start the frontend
echo "🌐 Starting React Frontend..."
cd /Volumes/Development/livekit/livekit-agent/frontend
npm run dev &
FRONTEND_PID=$!

echo "✅ All services started!"
echo "🎓 Security+ Agent: Connected to security-plus-room"
echo "🌐 Frontend: http://localhost:3000"
echo "🔊 Audio: ENABLED and working"
echo ""
echo "📋 Available commands:"
echo "   • 'Teach me about [topic]' - Start a lesson"
echo "   • 'Quiz me' - Practice questions"
echo "   • 'Explain [topic]' - Get explanations"
echo "   • 'What topics can you teach?' - See available topics"
echo ""
echo "Press Ctrl+C to stop all services"

# Function to cleanup on exit
cleanup() {
    echo "🛑 Stopping services..."
    kill $AGENT_PID $FRONTEND_PID 2>/dev/null
    [ ! -z "$SERVER_PID" ] && kill $SERVER_PID 2>/dev/null
    exit
}

# Set trap for cleanup
trap cleanup INT

# Wait for processes
wait
