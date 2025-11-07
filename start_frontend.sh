#!/bin/bash

# LiveKit Security+ Agent with Frontend
echo "🚀 Starting LiveKit Security+ Agent with Frontend..."

# Start the agent in dev mode (for frontend connections)
echo "📚 Starting Security+ Agent with Avatar in Dev Mode..."
cd /Volumes/Development/livekit/livekit-agent
uv run python security_plus_agent.py dev &
AGENT_PID=$!

# Wait a moment for agent to register
sleep 5

# Start the frontend
echo "🌐 Starting React Frontend..."
cd /Volumes/Development/livekit/livekit-agent/frontend
npm run dev &
FRONTEND_PID=$!

echo "✅ Both services started!"
echo "🎓 Security+ Agent: Running in dev mode (registered with LiveKit Cloud)"
echo "🌐 Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both services"

# Wait for both processes
trap "echo '🛑 Stopping services...'; kill $AGENT_PID $FRONTEND_PID; exit" INT
wait
