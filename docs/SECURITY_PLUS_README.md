# Security+ Exam Teaching Assistant

An interactive voice AI agent built with LiveKit that helps students prepare for the CompTIA Security+ (SY0-701) certification exam.

## Features

### 📚 Comprehensive Knowledge Base

The agent includes detailed coverage of all five Security+ exam domains:

1. **General Security Concepts (12%)**
   - Security controls (technical, managerial, operational, physical)
   - Fundamental security concepts (CIA Triad, non-repudiation, AAA, Zero Trust)
   - Change management processes
   - Cryptographic solutions (PKI, encryption, hashing, certificates)

2. **Threats, Vulnerabilities, and Mitigations (22%)**
   - Threat actors and motivations (nation-state, hacktivist, insider, organized crime)
   - Threat vectors and attack surfaces (email, SMS, social engineering, supply chain)
   - Vulnerability types (application, OS, hardware, cloud-specific, zero-day)
   - Indicators of malicious activity (malware, attacks, password attacks)
   - Mitigation techniques (segmentation, access control, patching, encryption)

3. **Security Architecture (18%)**
   - Security implications of architecture models (cloud, hybrid, IoT, ICS/SCADA)
   - Security principles for enterprise infrastructure (device placement, security zones)
   - Data protection methods (encryption, hashing, masking, tokenization)
   - Resilience and recovery (high availability, backups, disaster recovery)

4. **Security Operations (28%)**
   - Security techniques (hardening, wireless security, application security)
   - Asset management (acquisition, monitoring, disposal)
   - Vulnerability management (scanning, analysis, remediation)
   - Security alerting and monitoring (SIEM, IDS/IPS, log aggregation)
   - Identity and access management (provisioning, MFA, access controls)
   - Modifying enterprise capabilities (automation, incident response)
   - Using data sources (logs, vulnerability scans, packet captures)

5. **Security Program Management and Oversight (20%)**
   - Security governance (policies, standards, procedures)
   - Risk management (assessment, BIA, RTO/RPO, risk response strategies)
   - Third-party risk management (vendor assessment, agreements, monitoring)
   - Compliance and monitoring (reporting, audits, privacy)
   - Security awareness and training (phishing campaigns, user guidance)

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
4. **Focus on High-Weight Domains** - Security Operations (28%) and Security Program Management (20%) are the largest
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
