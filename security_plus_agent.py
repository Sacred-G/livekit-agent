"""
LiveKit Security+ Exam Teaching Assistant
==========================================
An interactive voice agent that helps students prepare for the CompTIA Security+ exam.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import random

load_dotenv(".env")

class SecurityPlusTeacher(Agent):
    """Security+ exam teaching assistant with comprehensive knowledge base."""

    def __init__(self):
        super().__init__(
            instructions="""You are an expert Security+ exam instructor helping students prepare for CompTIA Security+ certification.
            
            Your role is to:
            - Explain security concepts clearly and concisely
            - Provide examples and real-world scenarios
            - Quiz students on exam topics
            - Track their progress and identify weak areas
            - Offer study tips and exam strategies
            
            Keep responses conversational and encouraging. Break down complex topics into digestible pieces."""
        )

        # Initialize knowledge base and tracking
        self._init_knowledge_base()
        self._init_practice_questions()
        self.student_progress = {
            "questions_answered": 0,
            "correct_answers": 0,
            "topics_covered": set()
        }

    def _init_knowledge_base(self):
        """Initialize the Security+ knowledge base."""
        self.knowledge_base = {
            "domain_1": {
                "name": "Threats, Attacks, and Vulnerabilities",
                "weight": "24%",
                "topics": {
                    "malware": {
                        "description": "Malicious software designed to harm or exploit systems",
                        "types": [
                            "Virus - Attaches to files and spreads when executed",
                            "Worm - Self-replicating malware that spreads without user action",
                            "Trojan - Disguises itself as legitimate software",
                            "Ransomware - Encrypts data and demands payment",
                            "Spyware - Secretly monitors user activity",
                            "Rootkit - Hides malware presence at system level"
                        ],
                        "key_points": [
                            "Worms self-replicate, viruses need execution",
                            "Ransomware is a major threat to organizations",
                            "Rootkits are difficult to detect"
                        ]
                    },
                    "social_engineering": {
                        "description": "Psychological manipulation to trick users",
                        "types": [
                            "Phishing - Fraudulent emails requesting information",
                            "Spear Phishing - Targeted phishing attacks",
                            "Whaling - Phishing targeting executives",
                            "Vishing - Voice phishing via phone",
                            "Smishing - SMS phishing",
                            "Pretexting - Creating false scenarios",
                            "Tailgating - Following into secure areas"
                        ],
                        "key_points": [
                            "Exploits human psychology, not technical flaws",
                            "User awareness training is best defense",
                            "Always verify requests for sensitive data"
                        ]
                    },
                    "attacks": {
                        "description": "Common attack methods",
                        "types": [
                            "DoS/DDoS - Overwhelming systems with traffic",
                            "Man-in-the-Middle - Intercepting communications",
                            "SQL Injection - Malicious SQL code insertion",
                            "XSS - Cross-Site Scripting attacks",
                            "Password Attacks - Brute force, dictionary",
                            "Zero-Day - Exploiting unknown vulnerabilities"
                        ],
                        "key_points": [
                            "DDoS uses multiple sources",
                            "Injection attacks target input validation",
                            "Zero-days have no patches available"
                        ]
                    }
                }
            },
            "domain_2": {
                "name": "Architecture and Design",
                "weight": "21%",
                "topics": {
                    "security_concepts": {
                        "description": "Fundamental security principles",
                        "concepts": [
                            "CIA Triad - Confidentiality, Integrity, Availability",
                            "Non-repudiation - Proof that cannot be denied",
                            "Authentication - Verifying identity",
                            "Authorization - Granting access rights",
                            "Defense in Depth - Multiple security layers",
                            "Least Privilege - Minimum necessary access"
                        ],
                        "key_points": [
                            "CIA Triad is foundation of security",
                            "AAA: Authentication, Authorization, Accounting",
                            "Defense in depth uses layered security"
                        ]
                    },
                    "network_design": {
                        "description": "Secure network architecture",
                        "concepts": [
                            "DMZ - Demilitarized zone for public services",
                            "VLANs - Virtual LANs for segmentation",
                            "NAT - Network Address Translation",
                            "Zero Trust - Never trust, always verify",
                            "Network Segmentation - Isolating portions"
                        ],
                        "key_points": [
                            "DMZ protects internal network",
                            "Segmentation limits lateral movement",
                            "Zero trust assumes breach"
                        ]
                    },
                    "cloud_security": {
                        "description": "Cloud computing security",
                        "concepts": [
                            "IaaS - Infrastructure as a Service",
                            "PaaS - Platform as a Service",
                            "SaaS - Software as a Service",
                            "Shared Responsibility Model"
                        ],
                        "key_points": [
                            "Security responsibilities vary by model",
                            "Provider handles physical security",
                            "Customer responsible for data"
                        ]
                    }
                }
            },
            "domain_3": {
                "name": "Implementation",
                "weight": "25%",
                "topics": {
                    "cryptography": {
                        "description": "Encryption and cryptographic concepts",
                        "concepts": [
                            "Symmetric - Same key (AES, DES)",
                            "Asymmetric - Public/private keys (RSA, ECC)",
                            "Hashing - One-way function (SHA-256)",
                            "Digital Signatures - Verify authenticity",
                            "PKI - Public Key Infrastructure",
                            "SSL/TLS - Secure communication"
                        ],
                        "key_points": [
                            "Symmetric is fast, asymmetric is secure",
                            "Hashing is one-way, encryption is two-way",
                            "Digital signatures use private key"
                        ]
                    },
                    "authentication": {
                        "description": "Identity verification methods",
                        "concepts": [
                            "Something You Know - Password, PIN",
                            "Something You Have - Token, smart card",
                            "Something You Are - Biometrics",
                            "MFA - Multi-Factor Authentication",
                            "SSO - Single Sign-On",
                            "Kerberos - Ticket-based authentication"
                        ],
                        "key_points": [
                            "MFA significantly improves security",
                            "Biometrics have error rates",
                            "Kerberos uses tickets"
                        ]
                    },
                    "wireless_security": {
                        "description": "Securing wireless networks",
                        "protocols": [
                            "WEP - Deprecated, insecure",
                            "WPA - Wi-Fi Protected Access",
                            "WPA2 - Uses AES encryption",
                            "WPA3 - Latest standard"
                        ],
                        "key_points": [
                            "Never use WEP",
                            "WPA2 with AES is minimum",
                            "WPA3 provides enhanced protection"
                        ]
                    }
                }
            },
            "domain_4": {
                "name": "Operations and Incident Response",
                "weight": "16%",
                "topics": {
                    "incident_response": {
                        "description": "Handling security incidents",
                        "phases": [
                            "1. Preparation",
                            "2. Identification",
                            "3. Containment",
                            "4. Eradication",
                            "5. Recovery",
                            "6. Lessons Learned"
                        ],
                        "key_points": [
                            "Follow structured process",
                            "Document everything",
                            "Containment prevents damage"
                        ]
                    },
                    "monitoring": {
                        "description": "Security monitoring",
                        "tools": [
                            "SIEM - Security Information and Event Management",
                            "IDS - Intrusion Detection (passive)",
                            "IPS - Intrusion Prevention (active)",
                            "Log Aggregation"
                        ],
                        "key_points": [
                            "SIEM correlates events",
                            "IDS detects, IPS prevents",
                            "Logging essential for forensics"
                        ]
                    }
                }
            },
            "domain_5": {
                "name": "Governance, Risk, and Compliance",
                "weight": "14%",
                "topics": {
                    "policies": {
                        "description": "Security policies and procedures",
                        "types": [
                            "AUP - Acceptable Use Policy",
                            "Password Policy",
                            "Data Classification",
                            "Change Management",
                            "Business Continuity",
                            "Disaster Recovery"
                        ],
                        "key_points": [
                            "Policies define what",
                            "Procedures define how",
                            "Standards define requirements"
                        ]
                    },
                    "risk_management": {
                        "description": "Managing risks",
                        "concepts": [
                            "Risk Assessment",
                            "SLE - Single Loss Expectancy",
                            "ARO - Annual Rate of Occurrence",
                            "ALE - Annual Loss Expectancy",
                            "Risk Mitigation",
                            "Risk Transference",
                            "Risk Acceptance",
                            "Risk Avoidance"
                        ],
                        "key_points": [
                            "Risk cannot be eliminated",
                            "ALE = SLE × ARO",
                            "Choose appropriate response"
                        ]
                    }
                }
            }
        }

    def _init_practice_questions(self):
        """Initialize practice questions."""
        self.practice_questions = [
            {
                "question": "Which malware can replicate without user interaction?",
                "options": ["A) Virus", "B) Worm", "C) Trojan", "D) Rootkit"],
                "correct": "B",
                "explanation": "Worms self-replicate and spread across networks without user action."
            },
            {
                "question": "What does CIA triad stand for?",
                "options": ["A) Confidentiality, Integrity, Availability", "B) Control, Identity, Access", 
                           "C) Cryptography, Identification, Authentication", "D) Compliance, Investigation, Analysis"],
                "correct": "A",
                "explanation": "CIA Triad: Confidentiality, Integrity, and Availability - foundation of information security."
            },
            {
                "question": "Which encryption uses the same key for encrypt and decrypt?",
                "options": ["A) Asymmetric", "B) Symmetric", "C) Hashing", "D) Public key"],
                "correct": "B",
                "explanation": "Symmetric encryption uses same key for both operations. Fast but requires secure key distribution."
            },
            {
                "question": "What is the first phase of incident response?",
                "options": ["A) Containment", "B) Identification", "C) Preparation", "D) Eradication"],
                "correct": "C",
                "explanation": "Preparation is first - develop IR plan, train team, prepare tools before incidents occur."
            },
            {
                "question": "Which wireless protocol should NOT be used?",
                "options": ["A) WPA2", "B) WPA3", "C) WEP", "D) WPA"],
                "correct": "C",
                "explanation": "WEP is deprecated and easily cracked. Never use it. WPA2 or WPA3 are current standards."
            },
            {
                "question": "What attack intercepts communication between two parties?",
                "options": ["A) DoS", "B) Man-in-the-Middle", "C) Phishing", "D) SQL Injection"],
                "correct": "B",
                "explanation": "Man-in-the-Middle attacks secretly intercept and potentially alter communications."
            },
            {
                "question": "Which access control uses labels and clearances?",
                "options": ["A) DAC", "B) RBAC", "C) MAC", "D) ABAC"],
                "correct": "C",
                "explanation": "Mandatory Access Control (MAC) uses security labels and clearances. Most restrictive, used in military."
            },
            {
                "question": "What does MFA stand for?",
                "options": ["A) Multiple Factor Authentication", "B) Multi-Factor Authentication", 
                           "C) Managed File Access", "D) Mandatory Factor Authorization"],
                "correct": "B",
                "explanation": "Multi-Factor Authentication requires two or more factors from different categories to verify identity."
            }
        ]

    @function_tool
    async def get_exam_overview(self, context: RunContext) -> str:
        """Get overview of Security+ exam structure."""
        overview = "CompTIA Security+ (SY0-701) Exam:\n\n"
        overview += "• 90 questions (multiple choice and performance-based)\n"
        overview += "• 90 minutes duration\n"
        overview += "• Passing Score: 750 (scale 100-900)\n\n"
        overview += "Domains:\n"
        
        for domain_id, domain in self.knowledge_base.items():
            overview += f"• {domain['name']} - {domain['weight']}\n"
        
        return overview

    @function_tool
    async def explain_topic(self, context: RunContext, domain: str, topic: str) -> str:
        """Explain a specific Security+ topic.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., malware, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        explanation = f"📚 {topic.replace('_', ' ').title()}\n\n"
        explanation += f"{topic_data['description']}\n\n"
        
        if "types" in topic_data:
            explanation += "Types:\n"
            for item in topic_data["types"][:4]:
                explanation += f"• {item}\n"
        
        if "concepts" in topic_data:
            explanation += "Concepts:\n"
            for item in topic_data["concepts"][:4]:
                explanation += f"• {item}\n"
        
        if "phases" in topic_data:
            explanation += "Phases:\n"
            for item in topic_data["phases"]:
                explanation += f"• {item}\n"
        
        if "key_points" in topic_data:
            explanation += "\n🎯 Key Points:\n"
            for point in topic_data["key_points"]:
                explanation += f"• {point}\n"
        
        return explanation

    @function_tool
    async def list_topics(self, context: RunContext, domain: str) -> str:
        """List all topics in a domain.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
        """
        domain = domain.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use: domain_1, domain_2, domain_3, domain_4, or domain_5"
        
        domain_data = self.knowledge_base[domain]
        result = f"{domain_data['name']} ({domain_data['weight']})\n\n"
        
        for topic_key, topic_data in domain_data["topics"].items():
            result += f"• {topic_key}: {topic_data['description']}\n"
        
        return result

    @function_tool
    async def quiz_me(self, context: RunContext, num_questions: int = 1) -> str:
        """Start practice quiz.
        
        Args:
            num_questions: Number of questions (1-5)
        """
        num_questions = min(max(1, num_questions), 5)
        questions = random.sample(self.practice_questions, min(num_questions, len(self.practice_questions)))
        
        quiz_text = f"📝 Practice Quiz - {num_questions} Question(s)\n\n"
        
        for i, q in enumerate(questions, 1):
            quiz_text += f"Q{i}: {q['question']}\n"
            for option in q['options']:
                quiz_text += f"{option}\n"
            quiz_text += "\n"
        
        quiz_text += "Tell me your answer(s) - e.g., 'A' or 'B, C, A'"
        context.store_metadata("current_quiz", questions)
        
        return quiz_text

    @function_tool
    async def check_answer(self, context: RunContext, answer: str) -> str:
        """Check quiz answers.
        
        Args:
            answer: Your answer(s) (e.g., 'A' or 'B, C, A')
        """
        current_quiz = context.get_metadata("current_quiz")
        
        if not current_quiz:
            return "No active quiz. Use quiz_me first!"
        
        answers = [a.strip().upper() for a in answer.split(",")]
        
        if len(answers) != len(current_quiz):
            return f"Provide {len(current_quiz)} answer(s)"
        
        results = "📊 Results:\n\n"
        correct_count = 0
        
        for i, (ans, q) in enumerate(zip(answers, current_quiz), 1):
            is_correct = ans == q['correct']
            if is_correct:
                correct_count += 1
                self.student_progress["correct_answers"] += 1
                results += f"Q{i}: ✓ Correct!\n"
            else:
                results += f"Q{i}: ✗ Wrong. Answer: {q['correct']}\n"
            
            results += f"{q['explanation']}\n\n"
            self.student_progress["questions_answered"] += 1
        
        score = (correct_count / len(current_quiz)) * 100
        results += f"Score: {correct_count}/{len(current_quiz)} ({score:.0f}%)\n"
        
        if score == 100:
            results += "🎉 Perfect!"
        elif score >= 70:
            results += "👍 Good work!"
        else:
            results += "📚 Keep studying!"
        
        context.store_metadata("current_quiz", None)
        return results

    @function_tool
    async def get_study_tips(self, context: RunContext) -> str:
        """Get study tips for Security+ exam."""
        tips = "🎓 Security+ Study Tips:\n\n"
        tips += "1. Understand concepts, don't just memorize\n"
        tips += "2. Use acronyms (CIA, AAA, etc.)\n"
        tips += "3. Practice hands-on labs\n"
        tips += "4. Focus on high-weight domains (25% and 24%)\n"
        tips += "5. Read questions carefully on exam day\n"
        tips += "6. Watch for key words: BEST, MOST, FIRST\n"
        tips += "7. Performance-based questions come first\n"
        tips += "8. Flag difficult questions and return later\n"
        return tips

    @function_tool
    async def get_progress(self, context: RunContext) -> str:
        """Check your study progress."""
        progress = "📈 Your Progress:\n\n"
        progress += f"Questions Answered: {self.student_progress['questions_answered']}\n"
        progress += f"Correct: {self.student_progress['correct_answers']}\n"
        
        if self.student_progress['questions_answered'] > 0:
            accuracy = (self.student_progress['correct_answers'] / self.student_progress['questions_answered']) * 100
            progress += f"Accuracy: {accuracy:.1f}%\n"
        else:
            progress += "Accuracy: N/A\n"
        
        progress += f"\nTopics Covered: {len(self.student_progress['topics_covered'])}\n"
        
        return progress


async def entrypoint(ctx: agents.JobContext):
    """Entry point for the Security+ teaching agent."""
    
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model=os.getenv("LLM_CHOICE", "gpt-4o-mini")),
        tts=openai.TTS(voice="echo"),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=SecurityPlusTeacher()
    )

    await session.generate_reply(
        instructions="Greet the student warmly and introduce yourself as their Security+ exam tutor. Ask what they'd like to study today."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
