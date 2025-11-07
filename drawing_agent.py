"""
LiveKit Security+ Agent with Advanced Drawing Capabilities
=========================================================
An agent that can generate precise drawing instructions to create visual content on whiteboards.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext, JobContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import json
import math
from typing import Dict, List, Any

# Load environment variables
load_dotenv(".env")

class DrawingSecurityTeacher(Agent):
    """Security+ instructor that can generate drawing instructions to create visual content."""

    def __init__(self):
        super().__init__(
            instructions="""You are a certified CompTIA Security+ instructor who can create visual drawings through guided instructions.
            
            You can generate step-by-step drawing instructions that users can follow to create professional security diagrams.
            When users ask you to draw something, provide:
            1. Exact coordinates and positions
            2. Specific shapes and sizes
            3. Colors and styling details
            4. Step-by-step sequence
            5. Labels and annotations
            
            Always be precise about where to place elements on the canvas.
            Use a coordinate system where (0,0) is top-left corner.
            """
        )

    @function_tool
    async def draw_network_topology(self, context: RunContext, topology_type: str) -> str:
        """Generate drawing instructions for network security topologies."""
        
        if topology_type == "secure_network":
            return """
            🎯 Let's Draw a Secure Network Topology!
            
            Step 1: Draw Internet Cloud
            - Position: Top center (400, 50)
            - Shape: Large cloud outline
            - Color: Blue
            - Label: "Internet" inside
            
            Step 2: Draw External Firewall
            - Position: (350, 150) to (450, 200)
            - Shape: Rectangle with brick pattern
            - Color: Red/Orange brick colors
            - Label: "External Firewall" above
            
            Step 3: Draw DMZ Zone
            - Position: Rectangle (200, 250) to (600, 350)
            - Shape: Large rectangle border
            - Color: Light gray border
            - Label: "DMZ" at top
            
            Step 4: Add Web Server in DMZ
            - Position: (350, 280) to (450, 320)
            - Shape: Server rack rectangle
            - Color: Dark blue
            - Label: "Web Server"
            
            Step 5: Draw Internal Firewall
            - Position: (350, 400) to (450, 450)
            - Shape: Brick wall rectangle
            - Color: Red/Orange
            - Label: "Internal Firewall"
            
            Step 6: Draw Internal Network
            - Position: Rectangle (200, 500) to (600, 650)
            - Shape: Large rectangle border
            - Color: Green border
            - Label: "Internal Network"
            
            Step 7: Add Database Server
            - Position: (350, 550) to (450, 600)
            - Shape: Server cylinder
            - Color: Purple
            - Label: "Database"
            
            Step 8: Draw Connection Lines
            - Connect all elements with arrows
            - Color: Black for data flow
            - Add arrow heads showing direction
            
            Follow these steps exactly and I'll analyze your secure network design!
            """
        
        elif topology_type == "firewall_rules":
            return """
            🔥 Drawing Firewall Rules Visualization!
            
            Step 1: Draw Firewall Box
            - Position: Center (300, 200) to (500, 400)
            - Shape: Large rectangle
            - Color: Brick red/orange pattern
            - Label: "FIREWALL" at top
            
            Step 2: Draw Incoming Traffic (Left)
            - Position: Arrows from left edge
            - Color: Red for blocked, Green for allowed
            - Labels: "HTTP", "FTP", "SSH", "Malware"
            
            Step 3: Draw Outgoing Traffic (Right)
            - Position: Arrows to right edge
            - Color: Green for allowed
            - Labels: "HTTPS Response", "DNS"
            
            Step 4: Add Rule Table
            - Position: Bottom of firewall (320, 350) to (480, 450)
            - Shape: Table with rows
            - Content: 
              Row 1: ALLOW HTTP (80) ✓
              Row 2: DENY FTP (21) ✗
              Row 3: ALLOW SSH (22) ✓
              Row 4: DENY ALL ✗
            
            This shows how firewalls filter traffic based on rules!
            """

    @function_tool
    async def draw_encryption_process(self, context: RunContext, encryption_type: str) -> str:
        """Generate drawing instructions for encryption processes."""
        
        if encryption_type == "aes_encryption":
            return """
            🔐 Drawing AES Encryption Process!
            
            Step 1: Draw Plain Text Box
            - Position: (100, 200) to (250, 250)
            - Shape: Rectangle
            - Color: Light blue
            - Label: "Plain Text: HELLO"
            
            Step 2: Draw AES Algorithm Box
            - Position: (350, 180) to (450, 270)
            - Shape: Large rectangle with gear icon
            - Color: Purple
            - Label: "AES-256"
            
            Step 3: Draw Key Input
            - Position: Arrow from top (400, 100) to (400, 180)
            - Shape: Key symbol at top
            - Color: Gold/Yellow
            - Label: "256-bit Key"
            
            Step 4: Draw Cipher Text Box
            - Position: (550, 200) to (700, 250)
            - Shape: Rectangle with scrambled text
            - Color: Red
            - Label: "Cipher: X¥§‡×"
            
            Step 5: Draw Decryption Process
            - Position: Below encryption (mirror image)
            - Same boxes but reverse flow
            - Label: "Decryption"
            
            Step 6: Add Process Arrows
            - Connect all boxes with directional arrows
            - Color: Dark blue
            - Show bidirectional flow
            
            This visualizes how AES encryption transforms data!
            """
        
        elif encryption_type == "rsa_handshake":
            return """
            🤝 Drawing RSA Key Exchange!
            
            Step 1: Draw Client and Server Columns
            - Client: Left side (100, 100) to (300, 500)
            - Server: Right side (500, 100) to (700, 500)
            - Labels: "CLIENT" and "SERVER"
            
            Step 2: Draw Public Keys
            - Client public: (150, 150) circle
            - Server public: (550, 150) circle
            - Color: Blue
            - Labels: "Public Key"
            
            Step 3: Draw Private Keys
            - Client private: (150, 450) locked box
            - Server private: (550, 450) locked box
            - Color: Red
            - Labels: "Private Key (Secret)"
            
            Step 4: Draw Key Exchange Arrows
            - Client to Server: Public key arrow
            - Server to Client: Public key arrow
            - Color: Green for exchange
            
            Step 5: Draw Encrypted Communication
            - Middle section: Lock symbols
            - Color: Purple
            - Label: "Encrypted Channel"
            
            This shows how RSA enables secure communication!
            """

    @function_tool
    async def draw_protocol_diagram(self, context: RunContext, protocol: str) -> str:
        """Generate drawing instructions for protocol diagrams."""
        
        if protocol == "tcp_handshake":
            return """
            🤝 Drawing TCP Three-Way Handshake!
            
            Step 1: Setup Timeline
            - Draw vertical line at (200, 100) to (200, 500) - Client
            - Draw vertical line at (600, 100) to (600, 500) - Server
            - Labels: "CLIENT" and "SERVER"
            
            Step 2: Draw SYN Packet
            - From: (200, 150) to (600, 150)
            - Arrow pointing right
            - Label: "SYN (Seq=100)"
            - Color: Blue
            
            Step 3: Draw SYN-ACK Response
            - From: (600, 250) to (200, 250)
            - Arrow pointing left
            - Label: "SYN-ACK (Seq=300, Ack=101)"
            - Color: Green
            
            Step 4: Draw ACK Packet
            - From: (200, 350) to (600, 350)
            - Arrow pointing right
            - Label: "ACK (Seq=101, Ack=301)"
            - Color: Purple
            
            Step 5: Draw Connection Established
            - Position: Bottom (400, 450)
            - Shape: Green checkmark
            - Label: "✓ Connection Established"
            
            Step 6: Add Time Indicators
            - Small time marks on left
            - Show sequence timing
            
            This visualizes the TCP connection process!
            """

    @function_tool
    async def draw_attack_tree(self, context: RunContext, attack_type: str) -> str:
        """Generate drawing instructions for attack trees."""
        
        if attack_type == "data_breach":
            return """
            🌳 Drawing Data Breach Attack Tree!
            
            Step 1: Draw Root Goal
            - Position: Top center (400, 50)
            - Shape: Red rectangle
            - Label: "DATA BREACH"
            
            Step 2: Draw Primary Branches
            - Left branch: "Network Attack" at (200, 150)
            - Right branch: "Insider Threat" at (600, 150)
            - Color: Orange rectangles
            
            Step 3: Network Attack Sub-branches
            - From "Network Attack":
              * "Exploit Vulnerability" at (100, 250)
              * "Weak Passwords" at (200, 250)
              * "MITM Attack" at (300, 250)
            
            Step 4: Insider Threat Sub-branches
            - From "Insider Threat":
              * "Malicious Employee" at (500, 250)
              * "Accidental Exposure" at (600, 250)
              * "Social Engineering" at (700, 250)
            
            Step 5: Add Leaf Nodes
            - Under each sub-branch add specific techniques
            - Color: Light red
            - Examples: "SQL Injection", "Phishing", "Weak Auth"
            
            Step 6: Draw Mitigation Boxes
            - Position: Bottom row in green
            - Countermeasures for each path
            - Color: Green
            
            This maps all possible paths to a data breach!
            """

    @function_tool
    async def generate_drawing_coordinates(self, context: RunContext, element: str) -> str:
        """Generate precise coordinates for drawing security elements."""
        
        elements = {
            "firewall": "Draw rectangle at (300, 200) to (500, 300). Use brick pattern with red/orange colors.",
            "server": "Draw server rack at (350, 400) to (450, 550). Add horizontal lines and green/red status lights.",
            "router": "Draw cylinder at (400, 150) with radius 30. Add arrows pointing in 4 directions.",
            "switch": "Draw rectangle at (200, 350) to (300, 400). Add small connection circles on edges.",
            "database": "Draw cylinder at (500, 400) to (600, 500). Add horizontal lines and key symbol.",
            "user": "Draw stick figure at (100, 450). Add computer in front.",
            "cloud": "Draw cloud shape at (400, 50) covering (300,30) to (500,80).",
            "lock": "Draw padlock at (400, 300) with size 40x30. Add keyhole detail."
        }
        
        return elements.get(element, f"Draw {element} at appropriate position on canvas.")

    @function_tool
    async def create_security_diagram(self, context: RunContext, diagram_type: str) -> str:
        """Generate complete security diagram instructions."""
        
        diagrams = {
            "defense_in_depth": """
            🛡️ Drawing Defense in Depth Strategy!
            
            Layer 1 - Perimeter Security (Top):
            - Draw firewall at (300, 100) to (500, 150)
            - Add "External Firewall" label
            - Color: Red brick pattern
            
            Layer 2 - Network Security:
            - Draw IDS/IPS at (350, 200) to (450, 250)
            - Add sensor icons
            - Color: Orange
            
            Layer 3 - Host Security:
            - Draw server with antivirus at (350, 300) to (450, 350)
            - Add shield symbol
            - Color: Yellow
            
            Layer 4 - Application Security:
            - Draw application layer at (300, 400) to (500, 450)
            - Add code symbols
            - Color: Green
            
            Layer 5 - Data Security:
            - Draw encrypted database at (350, 500) to (450, 550)
            - Add lock symbols
            - Color: Blue
            
            Connect all layers with vertical arrows showing protection depth!
            """,
            
            "access_control_matrix": """
            📊 Drawing Access Control Matrix!
            
            Step 1: Draw Table Structure
            - Header row: (200, 100) to (700, 150)
            - Data rows: 5 rows of 50px height each
            - Columns: Resource, Admin, Manager, User, Guest
            
            Step 2: Fill Headers
            - Column headers: "Resource", "Admin", "Manager", "User", "Guest"
            - Row headers: "Files", "Database", "Network", "Admin Panel", "Reports"
            
            Step 3: Add Permissions
            - Admin row: RWE, RWE, RWE, RWE, RWE (all green)
            - Manager row: RW, RW, R, R, RW (mostly green)
            - User row: R, R, R, (empty), R (some green)
            - Guest row: (empty), (empty), R, (empty), (empty) (mostly red)
            
            Step 4: Add Legend
            - Bottom: R=Read (green), W=Write (blue), E=Execute (purple)
            
            This visualizes role-based access control!
            """
        }
        
        return diagrams.get(diagram_type, "Diagram type not found. Try: defense_in_depth, access_control_matrix")

async def entrypoint(ctx: JobContext):
    """Entry point for the drawing-enabled agent."""
    
    print(f"🎨 Drawing Security+ agent starting in room: {ctx.room.name}")
    
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
        agent=DrawingSecurityTeacher(),
        room_input_options=agents.RoomInputOptions(
            video_enabled=True,  # Enable video for whiteboard sharing
        ),
        room_output_options=agents.RoomOutputOptions(
            audio_enabled=True,  # Enable audio output
        )
    )

    print("✅ Drawing Security+ agent started successfully!")
    
    # Generate initial greeting mentioning drawing capabilities
    await session.generate_reply(
        instructions="Greet the user as a Security+ instructor with advanced drawing capabilities. Emphasize that you can provide step-by-step drawing instructions to create professional security diagrams. Mention that you can generate precise coordinates and visual guides for network topologies, encryption processes, protocol diagrams, and attack trees. Be enthusiastic about helping them create visual study materials!"
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
