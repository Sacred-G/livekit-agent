"""
LiveKit Security+ Agent with Vision Support
============================================
An agent that can both speak and see screen content for interactive learning.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext, JobContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import base64
from PIL import Image
import io
from interactive_content import INTERACTIVE_PROMPTS, SAMPLE_CIPHERS, SAMPLE_PORT_SCAN

# Load environment variables
load_dotenv(".env")

class VisionSecurityTeacher(Agent):
    """Security+ instructor with vision capabilities."""

    def __init__(self):
        super().__init__(
            instructions="""You are a certified CompTIA Security+ instructor who can both hear and see.
            
            You have vision capabilities and can analyze screen content when shared. When users share their screen:
            1. Acknowledge that you can see their screen
            2. Describe what you see in detail
            3. Relate it to Security+ concepts when relevant
            4. Answer questions about the visual content
            
            For regular voice interactions:
            - Speak clearly and conversationally
            - Help with Security+ exam preparation
            - Keep responses engaging but concise
            
            When someone shares their screen, say "I can see your screen now! What would you like me to help you with?"
            """
        )

    @function_tool
    async def analyze_screen_content(self, context: RunContext) -> str:
        """Analyze the current screen content being shared."""
        return "I can see your screen! Please tell me what you'd like me to analyze or explain about what you're showing."

    @function_tool
    async def start_network_exercise(self, context: RunContext) -> str:
        """Start an interactive network security design exercise."""
        return INTERACTIVE_PROMPTS["network_design"]

    @function_tool
    async def start_cipher_challenge(self, context: RunContext) -> str:
        """Start a cryptography decryption challenge."""
        return INTERACTIVE_PROMPTS["cipher_challenge"]

    @function_tool
    async def start_incident_response(self, context: RunContext) -> str:
        """Start an incident response planning exercise."""
        return INTERACTIVE_PROMPTS["incident_response"]

    @function_tool
    async def get_port_scan_challenge(self, context: RunContext) -> str:
        """Get port scan results for security analysis."""
        return f"Here are port scan results to analyze:\n\n{SAMPLE_PORT_SCAN}\n\nDraw your analysis on screen and I'll review it!"

    @function_tool
    async def list_interactive_exercises(self, context: RunContext) -> str:
        """List all available interactive exercises."""
        exercises = """
        🎯 Available Interactive Exercises:
        
        📐 Network Design - Draw secure network topologies
        🔐 Cipher Challenges - Decrypt secret messages  
        🚨 Incident Response - Design security response plans
        🔍 Port Analysis - Analyze scan results for vulnerabilities
        📊 Access Control - Create permission matrices
        🤝 Protocol Analysis - Draw handshake processes
        
        Just say 'start [exercise name]' to begin any exercise!
        """
        return exercises

async def entrypoint(ctx: JobContext):
    """Entry point for the vision-enabled agent."""
    
    print(f"👁️ Vision Security+ agent starting in room: {ctx.room.name}")
    
    # Configure the voice pipeline with vision
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model="gpt-4o"),  # Vision-capable model
        tts=openai.TTS(voice="echo"),
        vad=silero.VAD.load(),
    )

    # Start the session with video input enabled for screen sharing
    await session.start(
        room=ctx.room,
        agent=VisionSecurityTeacher(),
        room_input_options=agents.RoomInputOptions(
            video_enabled=True,  # Enable video for screen sharing
        ),
        room_output_options=agents.RoomOutputOptions(
            audio_enabled=True,  # Enable audio output
        )
    )

    print("✅ Vision Security+ agent started successfully!")
    
    # Generate initial greeting mentioning vision capability
    await session.generate_reply(
        instructions="Greet the user warmly as a Security+ instructor. Mention that you can both hear them and see their screen if they choose to share it, which is great for reviewing diagrams, configurations, or practice questions. Ask how you can help with their Security+ studies today."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
