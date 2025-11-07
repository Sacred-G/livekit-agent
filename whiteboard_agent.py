"""
LiveKit Security+ Agent with Interactive Whiteboard
===================================================
An advanced agent that can both see and draw on a shared whiteboard for collaborative learning.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext, JobContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import json
import base64
from typing import Dict, List, Any
import asyncio

# Load environment variables
load_dotenv(".env")

class WhiteboardSecurityTeacher(Agent):
    """Security+ instructor with interactive whiteboard capabilities."""

    def __init__(self):
        super().__init__(
            instructions="""You are a certified CompTIA Security+ instructor with an interactive whiteboard.
            
            You can both see what users draw AND generate drawing instructions to create visual content.
            When users share their screen with a whiteboard app, you can:
            1. Analyze their drawings and diagrams
            2. Provide step-by-step drawing instructions for security concepts
            3. Suggest visual improvements and corrections
            4. Create collaborative diagrams by describing what to draw
            
            Always be encouraging and make learning visual and interactive!
            """
        )

    @function_tool
    async def start_whiteboard_exercise(self, context: RunContext, exercise_type: str) -> str:
        """Start an interactive whiteboard exercise with drawing instructions."""
        
        exercises = {
            "network_firewall": """
            🎯 Network Firewall Exercise!
            
            Let's draw a secure network architecture together:
            
            Step 1: Draw the Internet cloud at the top
            Step 2: Add a firewall (draw as a brick wall icon)
            Step 3: Create a DMZ section with a web server
            Step 4: Add another firewall
            Step 5: Draw the internal network with database
            
            Share your whiteboard screen and I'll guide you through each step!
            """,
            
            "encryption_flow": """
            🔐 Encryption Flow Diagram!
            
            Let's visualize how encryption works:
            
            Step 1: Draw "Plain Text" in a box
            Step 2: Draw an encryption algorithm box
            Step 3: Show the key entering the algorithm
            Step 4: Draw "Cipher Text" output
            Step 5: Show decryption process
            
            I'll help you make it technically accurate!
            """,
            
            "tcp_handshake": """
            🤝 TCP Three-Way Handshake!
            
            Let's draw the handshake process:
            
            Step 1: Draw two columns: "Client" and "Server"
            Step 2: Draw arrow from Client: "SYN"
            Step 3: Draw arrow from Server: "SYN-ACK" 
            Step 4: Draw arrow from Client: "ACK"
            Step 5: Add "Connection Established!"
            
            Share your screen and I'll check your timing diagram!
            """,
            
            "attack_tree": """
            🌳 Security Attack Tree Analysis!
            
            Let's map out potential security threats:
            
            Step 1: Draw "Data Breach" at the top
            Step 2: Branch to "Network Attack" and "Insider Threat"
            Step 3: Add sub-branches for specific attack types
            Step 4: Include mitigation strategies
            
            This is a powerful risk analysis technique!
            """
        }
        
        return exercises.get(exercise_type, "Unknown exercise type. Try: network_firewall, encryption_flow, tcp_handshake, or attack_tree.")

    @function_tool
    async def get_drawing_instructions(self, context: RunContext, concept: str) -> str:
        """Get step-by-step drawing instructions for security concepts."""
        
        instructions = {
            "firewall": """
            🔥 How to Draw a Firewall:
            
            1. Draw a rectangle shape (brick wall pattern)
            2. Add small rectangular "bricks" inside
            3. Draw arrows going through some bricks (allowed traffic)
            4. Draw red X's on blocked arrows (denied traffic)
            5. Label "ALLOWED" and "BLOCKED"
            
            This shows how firewalls filter traffic!
            """,
            
            "dmz": """
            🏢 How to Draw a DMZ:
            
            1. Draw three horizontal zones
            2. Top zone: "Internet" 
            3. Middle zone: "DMZ" (smaller)
            4. Bottom zone: "Internal Network" (largest)
            5. Draw firewalls between zones
            6. Place web server in DMZ, database in internal
            
            This shows secure network segmentation!
            """,
            
            "encryption": """
            🔐 How to Draw Encryption:
            
            1. Draw "PLAIN TEXT" in clear box
            2. Draw lock/algorithm box in middle
            3. Draw key symbol going into algorithm
            4. Draw "CIPHER TEXT" in scrambled box
            5. Show reverse process for decryption
            
            Visualize the transformation process!
            """
        }
        
        return instructions.get(concept, f"I don't have drawing instructions for '{concept}' yet. Try: firewall, dmz, or encryption.")

    @function_tool
    async def analyze_whiteboard(self, context: RunContext) -> str:
        """Analyze the current whiteboard content and provide feedback."""
        return "I can see your whiteboard! Great work. Let me analyze what you've drawn and provide some feedback for improvement."

    @function_tool
    async def suggest_improvements(self, context: RunContext, diagram_type: str) -> str:
        """Suggest improvements for specific diagram types."""
        
        suggestions = {
            "network": """
            📐 Network Diagram Improvements:
            
            ✅ Add these elements:
            - IP addresses and subnets
            - Port numbers on firewalls
            - IDS/IPS sensor locations
            - VPN gateway for remote access
            - Backup network connections
            
            🔍 Check these security aspects:
            - No direct internal-to-Internet connections
            - Proper DMZ isolation
            - Redundant firewall rules
            """,
            
            "encryption": """
            🔐 Encryption Diagram Improvements:
            
            ✅ Add these details:
            - Key length (AES-256, RSA-2048)
            - Algorithm names
            - Hash functions for integrity
            - Certificate authorities
            - Perfect forward secrecy
            
            🎯 Show these concepts:
            - Public vs private keys
            - Symmetric vs asymmetric
            - Key exchange protocols
            """
        }
        
        return suggestions.get(diagram_type, f"I'll provide specific suggestions for {diagram_type} diagrams!")

    @function_tool
    async def collaborative_drawing(self, context: RunContext, element: str) -> str:
        """Provide instructions for drawing specific security elements."""
        
        elements = {
            "router": "Draw a cylinder with arrows showing traffic routing between networks",
            "switch": "Draw a box with multiple connection points for local devices", 
            "server": "Draw a rectangle tower with horizontal lines to indicate rack mounting",
            "firewall": "Draw a brick wall pattern with some arrows passing through",
            "ids": "Draw a sensor icon with alert signals coming out",
            "vpn": "Draw a tunnel with encrypted data packets traveling through",
            "certificate": "Draw a document with a seal/stamp of authenticity",
            "key": "Draw a classic key shape for encryption concepts"
        }
        
        return f"Draw this element: {elements.get(element, f'Draw a {element} for your security diagram')}"

async def entrypoint(ctx: JobContext):
    """Entry point for the whiteboard-enabled agent."""
    
    print(f"🎨 Whiteboard Security+ agent starting in room: {ctx.room.name}")
    
    # Configure the voice pipeline with vision
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model="gpt-4o"),  # Vision-capable model
        tts=openai.TTS(voice="echo"),
        vad=silero.VAD.load(),
    )

    # Start the session with video input enabled
    await session.start(
        room=ctx.room,
        agent=WhiteboardSecurityTeacher(),
        room_input_options=agents.RoomInputOptions(
            video_enabled=True,  # Enable video for whiteboard sharing
        ),
        room_output_options=agents.RoomOutputOptions(
            audio_enabled=True,  # Enable audio output
        )
    )

    print("✅ Whiteboard Security+ agent started successfully!")
    
    # Generate initial greeting mentioning whiteboard capability
    await session.generate_reply(
        instructions="Greet the user as a Security+ instructor with interactive whiteboard capabilities. Mention that you can both see their drawings AND provide step-by-step instructions for creating security diagrams. Suggest starting with a simple network topology or encryption flow diagram. Be enthusiastic about making security learning visual and hands-on!"
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
