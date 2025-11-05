"""
Security+ Practice Questions
=============================
Practice quiz questions for CompTIA Security+ (SY0-701) exam.

NOTE: The main knowledge base has been moved to the 'domains' package.
This file now only contains practice questions for the quiz feature.
"""

# The comprehensive knowledge base is now in: domains/domain_1/knowledge.py through domain_5/knowledge.py
# Agent imports ALL_DOMAINS from domains package instead of using this file's old KNOWLEDGE_BASE

PRACTICE_QUESTIONS = [
    {
        "question": "Which malware can replicate without user interaction?",
        "options": ["A) Virus", "B) Worm", "C) Trojan", "D) Rootkit"],
        "correct": "B",
        "explanation": "Worms self-replicate and spread across networks without user action.",
    },
    {
        "question": "What does CIA Triad stand for?",
        "options": [
            "A) Confidentiality, Integrity, Availability",
            "B) Control, Identity, Access",
            "C) Cryptography, Identification, Authentication",
            "D) Compliance, Investigation, Analysis",
        ],
        "correct": "A",
        "explanation": "The CIA Triad is Confidentiality, Integrity, Availability.",
    },
    {
        "question": "Which encryption uses the same key for encrypt/decrypt?",
        "options": ["A) Asymmetric", "B) Symmetric", "C) Hashing", "D) Public Key"],
        "correct": "B",
        "explanation": "Symmetric encryption uses one shared key.",
    },
]