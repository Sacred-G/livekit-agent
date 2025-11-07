#!/bin/bash

# Deploy Security+ Agent to LiveKit Cloud
echo "🚀 Deploying Security+ Agent to LiveKit Cloud..."

# Navigate to agent directory
cd /Volumes/Development/livekit/livekit-agent

# Deploy the agent with a specific name
echo "📚 Deploying security-plus-agent with avatar..."
uv run livekit-cli deploy \
  --name security-plus-agent \
  --script security_plus_agent.py

echo "✅ Agent deployed successfully!"
echo ""
echo "🌐 Frontend should now connect to your Security+ agent with avatar"
echo "🎓 Your agent will have session persistence and remember Steven's progress"
