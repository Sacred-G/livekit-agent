# Security+ Exam Teaching Assistant

An interactive voice AI agent built with LiveKit that helps students prepare for the CompTIA Security+ (SY0-701) certification exam.

## Features

### 📚 Comprehensive Knowledge Base

The agent includes detailed coverage of all five Security+ exam domains:

1. **Threats, Attacks, and Vulnerabilities (24%)**
   - Malware types (viruses, worms, trojans, ransomware, etc.)
   - Social engineering attacks (phishing, vishing, pretexting, etc.)
   - Attack types (DoS/DDoS, MitM, SQL injection, XSS, etc.)

2. **Architecture and Design (21%)**
   - Security concepts (CIA triad, defense in depth, least privilege)
   - Network design (DMZ, VLANs, zero trust)
   - Cloud security (IaaS, PaaS, SaaS, shared responsibility)

3. **Implementation (25%)**
   - Cryptography (symmetric, asymmetric, hashing, PKI)
   - Authentication methods (MFA, SSO, Kerberos)
   - Wireless security (WPA2, WPA3, avoiding WEP)

4. **Operations and Incident Response (16%)**
   - Incident response phases (Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned)
   - Security monitoring (SIEM, IDS/IPS)

5. **Governance, Risk, and Compliance (14%)**
   - Security policies and procedures
   - Risk management (SLE, ARO, ALE)
   - Risk response strategies

### 🎯 Interactive Functions

The agent provides several voice-activated functions:

- **`get_exam_overview()`** - Get exam structure and domain breakdown
- **`list_topics(domain)`** - List all topics in a specific domain
- **`explain_topic(domain, topic)`** - Get detailed explanation of any topic
- **`quiz_me(num_questions)`** - Take a practice quiz (1-5 questions)
- **`check_answer(answer)`** - Check your quiz answers and get explanations
- **`get_study_tips()`** - Get exam strategies and study recommendations
- **`get_progress()`** - View your study statistics and accuracy

### 📝 Practice Questions

Includes 8 practice questions covering key exam topics with:
- Multiple choice options
- Correct answers
- Detailed explanations

## Usage

### Running the Agent

```bash
# Make sure you're in the livekit-agent directory
cd livekit-agent

# Run the Security+ agent
python security_plus_agent.py dev
```

### Example Interactions

**Getting Started:**
- "Give me an exam overview"
- "What topics are in domain 1?"
- "List topics in domain 3"

**Learning:**
- "Explain malware from domain 1"
- "Tell me about cryptography"
- "What is social engineering?"

**Practice:**
- "Quiz me with 3 questions"
- "My answer is B"
- "Check my answers: A, C, B"

**Progress Tracking:**
- "Show my progress"
- "Give me study tips"

## Knowledge Base Structure

The knowledge base is organized hierarchically:

```
Domain → Topics → Content
```

Each topic includes:
- **Description** - Brief overview
- **Types/Concepts** - Specific items to learn
- **Key Points** - Critical takeaways for the exam

## Study Tips

1. **Understand, Don't Memorize** - Focus on understanding WHY security measures are important
2. **Use Acronyms** - CIA (Confidentiality, Integrity, Availability), AAA (Authentication, Authorization, Accounting)
3. **Practice Hands-On** - Set up virtual labs to practice concepts
4. **Focus on High-Weight Domains** - Implementation (25%) and Threats (24%) are the largest
5. **Read Carefully** - Watch for keywords like "BEST", "MOST", "FIRST" on the exam

## Exam Information

- **Exam Code:** SY0-701
- **Questions:** 90 (multiple choice and performance-based)
- **Duration:** 90 minutes
- **Passing Score:** 750 (on a scale of 100-900)
- **Performance-Based Questions:** Appear first in the exam

## Customization

### Adding More Questions

Edit the `_init_practice_questions()` method in `security_plus_agent.py`:

```python
self.practice_questions.append({
    "question": "Your question here?",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "correct": "A",
    "explanation": "Explanation of the correct answer"
})
```

### Expanding the Knowledge Base

Add topics to the `_init_knowledge_base()` method:

```python
"new_topic": {
    "description": "Topic description",
    "types": ["Item 1", "Item 2"],
    "key_points": ["Point 1", "Point 2"]
}
```

## Requirements

- Python 3.9+
- LiveKit Agents framework
- OpenAI API key (for LLM and TTS)
- Deepgram API key (for STT)
- Environment variables in `.env` file

## Tips for Best Results

1. **Speak Clearly** - The voice recognition works best with clear speech
2. **Use Function Names** - Explicitly mention functions like "quiz me" or "explain topic"
3. **Be Specific** - When asking about topics, use the exact topic names from `list_topics`
4. **Take Notes** - While the agent tracks progress, keep your own notes for review
5. **Regular Practice** - Use the quiz function regularly to reinforce learning

## Next Steps

After mastering the basics with this agent:

1. Take full-length practice exams
2. Practice performance-based questions with hands-on labs
3. Review official CompTIA Security+ study materials
4. Join study groups or forums
5. Schedule your exam when consistently scoring 85%+ on practice tests

Good luck with your Security+ certification! 🎓
