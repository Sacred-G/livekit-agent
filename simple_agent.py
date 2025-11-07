"""
Simple LiveKit Security+ Agent for Audio Testing
===============================================
A minimal agent to test audio functionality without avatar complications.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.plugins import openai, deepgram, silero
import os

# Load environment variables
load_dotenv(".env")

class SimpleSecurityTeacher(Agent):
    """Simple Security+ instructor for audio testing."""

    def __init__(self):
        super().__init__(
            instructions="""You are a friendly CompTIA Security+ instructor.
            Speak clearly and conversationally. Keep responses brief but engaging.
            When someone joins, greet them warmly and offer to help with Security+ topics.
            Test your audio by asking if they can hear you clearly."""
        )

async def entrypoint(ctx: agents.JobContext):
    """Entry point for the simple agent."""
    
    print(f"🎤 Simple agent starting in room: {ctx.room.name}")
    
    # Configure the voice pipeline
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model=os.getenv("LLM_CHOICE", "gpt-4.1-mini")),
        tts=openai.TTS(voice="echo"),  # Using echo voice for clear audio
        vad=silero.VAD.load(),
    )

    # Start the session with audio enabled
    await session.start(
        room=ctx.room,
        agent=SimpleSecurityTeacher(),
        room_output_options=agents.RoomOutputOptions(
            audio_enabled=True,  # Ensure audio is enabled
        )
    )

    print("✅ Simple agent started successfully!")
    
    # Generate initial greeting to test audio
    await session.generate_reply(
        instructions="Greet the user warmly and ask if they can hear you clearly. This is a test of the audio system."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
