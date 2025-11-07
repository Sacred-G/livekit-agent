"""
Interactive Security+ Content for Screen Sharing
===============================================
Hands-on exercises, diagrams, and simulations that the agent can guide users through.
"""

import json
from typing import Dict, List, Any

class InteractiveContent:
    """Interactive Security+ exercises and visual content."""
    
    def __init__(self):
        self.exercises = {
            "network_topology": {
                "title": "Network Security Topology Design",
                "description": "Design a secure network topology",
                "instructions": """
                Draw a network topology that includes:
                1. DMZ with web server
                2. Internal network with database
                3. Firewall placement
                4. IDS/IPS sensors
                5. Remote access VPN
                
                Share your screen and I'll analyze your design!
                """,
                "elements_to_check": [
                    "Firewall between internet and DMZ",
                    "Firewall between DMZ and internal network",
                    "Web server in DMZ",
                    "Database in internal network",
                    "IDS/IPS placement",
                    "VPN concentrator"
                ]
            },
            "encryption_demo": {
                "title": "Encryption Process Visualization",
                "description": "Draw the encryption/decryption process",
                "instructions": """
                Draw a diagram showing:
                1. Plain text input
                2. Encryption algorithm
                3. Key generation process
                4. Cipher text output
                5. Decryption process
                6. Original text recovery
                
                I'll help you understand each step!
                """,
                "concepts": ["Symmetric encryption", "Asymmetric encryption", "Hash functions"]
            },
            "access_control_matrix": {
                "title": "Access Control Matrix",
                "description": "Create a role-based access control matrix",
                "instructions": """
                Create a table with:
                - Rows: User roles (Admin, Manager, User, Guest)
                - Columns: Resources (Files, Database, Network, Admin panel)
                - Cells: Permissions (Read, Write, Execute, None)
                
                Share your screen and I'll review your access control design!
                """,
                "security_principles": ["Least privilege", "Separation of duties", "Need to know"]
            },
            "incident_response_flow": {
                "title": "Incident Response Flowchart",
                "description": "Design an incident response process",
                "instructions": """
                Create a flowchart showing:
                1. Detection phase
                2. Analysis phase  
                3. Containment strategies
                4. Eradication steps
                5. Recovery process
                6. Lessons learned
                
                I'll evaluate your incident response plan!
                """,
                "phases": ["Preparation", "Detection", "Analysis", "Containment", "Eradication", "Recovery"]
            },
            "cipher_challenge": {
                "title": "Cipher Text Challenge",
                "description": "Decrypt a message and explain the process",
                "instructions": """
                I'll show you an encrypted message. Your task:
                1. Identify the cipher type
                2. Decrypt the message
                3. Explain the decryption steps
                4. Discuss the cipher's security
                
                Share your screen with your work and I'll guide you!
                """,
                "cipher_types": ["Caesar", "Vigenère", "AES", "RSA"]
            },
            "port_scanning_analysis": {
                "title": "Port Scan Results Analysis", 
                "description": "Analyze port scan results and identify vulnerabilities",
                "instructions": """
                I'll show you port scan results. Your task:
                1. Identify open ports and services
                2. Spot potential vulnerabilities
                3. Recommend remediation steps
                4. Prioritize findings by risk
                
                Share your analysis on screen and I'll help!
                """,
                "common_ports": {
                    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
                    53: "DNS", 80: "HTTP", 443: "HTTPS", 3389: "RDP"
                }
            }
        }
        
        self.diagrams = {
            "tcp_handshake": {
                "title": "TCP Three-Way Handshake",
                "description": "Draw and explain the TCP handshake process",
                "steps": [
                    "Client sends SYN",
                    "Server responds with SYN-ACK", 
                    "Client sends ACK",
                    "Connection established"
                ]
            },
            "ssl_tls_handshake": {
                "title": "SSL/TLS Handshake",
                "description": "Illustrate the secure connection setup",
                "steps": [
                    "Client Hello",
                    "Server Hello + Certificate",
                    "Key exchange",
                    "Finished messages"
                ]
            }
        }
    
    def get_exercise(self, name: str) -> Dict[str, Any]:
        """Get a specific interactive exercise."""
        return self.exercises.get(name, {})
    
    def get_diagram(self, name: str) -> Dict[str, Any]:
        """Get a specific diagram exercise."""
        return self.diagrams.get(name, {})
    
    def list_all_exercises(self) -> List[str]:
        """List all available interactive exercises."""
        return list(self.exercises.keys())
    
    def generate_cipher_challenge(self) -> Dict[str, str]:
        """Generate a cipher text challenge."""
        challenges = [
            {
                "type": "Caesar Cipher",
                "encrypted": "KHOOR ZRUOG",
                "hint": "Shift of 3",
                "answer": "HELLO WORLD"
            },
            {
                "type": "Atbash Cipher", 
                "encrypted": "SVOOL DLIOW",
                "hint": "Reverse alphabet",
                "answer": "HELLO WORLD"
            }
        ]
        return challenges[0]  # Return first challenge for simplicity

# Sample port scan results for exercises
SAMPLE_PORT_SCAN = """
Target: 192.168.1.100
Open ports: 22, 80, 443, 3389, 5900
Services: SSH, HTTP, HTTPS, RDP, VNC
"""

# Sample cipher text for challenges
SAMPLE_CIPHERS = {
    "caesar": {
        "encrypted": "FRQJUDWXODWLRQV RQ \RXU VHFULWB",
        "shift": 3,
        "hint": "Each letter is shifted forward in the alphabet"
    },
    "base64": {
        "encrypted": "SGVsbG8gV29ybGQ=",
        "hint": "This looks like Base64 encoding"
    }
}

# Interactive content prompts for the agent
INTERACTIVE_PROMPTS = {
    "network_design": """
    Let's do a hands-on network security exercise! 
    
    Please draw a network topology on your screen showing:
    🌐 Internet connection
    🔥 External firewall  
    🏢 DMZ with web server
    🔥 Internal firewall
    🏢 Internal network with:
       - Database server
       - User workstations
       - Domain controller
    🛡️ IDS/IPS sensors
    🔐 VPN for remote access
    
    Share your screen when ready and I'll analyze your security design!
    """,
    
    "cipher_challenge": """
    Time for a cryptography challenge! 
    
    Here's your encrypted message:
    
    📝 FRQJUDWXODWLRQV RQ \RXU VHFULWB
    
    Your mission:
    1️⃣ Identify the cipher type
    2️⃣ Decrypt the message  
    3️⃣ Show your work on screen
    4️⃣ Explain how you solved it
    
    Share your screen with your analysis and I'll guide you through it!
    """,
    
    "incident_response": """
    Let's design an incident response plan!
    
    Create a flowchart on your screen showing the complete incident response lifecycle:
    
    🚨 Detection → 📊 Analysis → 🛡️ Containment → 🧹 Eradication → 🔄 Recovery → 📚 Lessons Learned
    
    For each phase, add:
    - Key activities
    - Responsible teams
    - Tools needed
    - Success criteria
    
    Share your flowchart and I'll evaluate your incident response strategy!
    """
}
