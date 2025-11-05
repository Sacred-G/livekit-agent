# Lesson Functions Quick Reference

## All Available Lesson Functions

The Security+ agent has **3 ways** to deliver lesson content plus additional helper functions:

---

## 📖 Content Delivery Functions

### 1. `explain_topic(domain, topic)`
**Best for:** Quick reference and factual information

**Returns:** Structured explanation with categories and key points

**Voice Command:**
```
"Explain security controls from domain 1"
"Tell me about cryptography from domain 1"
```

**Example Output:**
```
📚 Security Controls

Various types of security controls and their purposes

Categories:
• Technical - Implemented through technology...
• Managerial - Administrative controls...
• Operational - Day-to-day operations...
• Physical - Physical security measures...

Control Types:
• Preventive - Prevent security incidents...
• Deterrent - Discourage potential attackers...

🎯 Key Points:
• Defense in depth uses multiple control types
• Controls work together for comprehensive security
```

---

### 2. `teach_lesson(domain, topic)`
**Best for:** Classroom-style interactive teaching

**Returns:** Conversational lesson with teaching language

**Voice Command:**
```
"Teach me about security controls from domain 1"
"Give me a lesson on cryptography"
```

**Example Output:**
```
📚 Today's Lesson: Security Controls

Alright class, today we're going to cover security controls. 
This is an important topic for your Security+ exam.

Let me start with the fundamentals. Various types of security 
controls and their purposes...

Let me pause here for a moment so you can write that down.

Now, let me walk you through the categories you need to know:

1. Technical - Implemented through technology...
2. Managerial - Administrative controls...

Take a moment to note these down. These are exam favorites.

🎯 Here are the critical points you absolutely must remember:
• Defense in depth uses multiple control types
• Controls work together for comprehensive security

These often appear on the exam, so highlight them in your notes.

Now, before we move on - do you have any questions?
```

---

### 3. `deliver_scripted_lesson(domain, topic)` 🆕
**Best for:** Polished, pre-written lesson scripts

**Returns:** Exact scripted content (verbatim)

**Voice Command:**
```
"Deliver the scripted lesson on security controls from domain 1"
"Give me the scripted lesson for security controls"
"Read the security controls script"
```

**Example Output:**
```
📚 Scripted Lesson: Security Controls

Domain: General Security Concepts

Let's be real, no prevention is ever perfect. So, what happens 
if an attacker gets past that first line? Well, that's where 
detective controls come in. Their job isn't to stop the 
incident, but to identify it and sound the alarm...

[Continues with full pre-written script]
```

**Note:** Only available for topics with a `scripted_lesson` field  
**Currently available:** domain_1/security_controls

---

## 📋 Helper Functions

### 4. `list_topics(domain)`
**Purpose:** See all available topics in a domain

**Voice Command:**
```
"List topics in domain 1"
"What topics are in domain 4?"
```

**Example Output:**
```
General Security Concepts (12%)

• security_controls: Various types of security controls...
• fundamental_concepts: Core security principles...
• zero_trust: Zero Trust architecture and principles...
• physical_security: Physical security controls...
• deception_technology: Deception and disruption technologies...
• change_management: Change management processes...
• cryptography: Cryptographic solutions and implementations...
```

---

### 5. `get_exam_overview()`
**Purpose:** See overall exam structure

**Voice Command:**
```
"Give me an exam overview"
"Show me the exam structure"
```

**Example Output:**
```
CompTIA Security+ (SY0-701) Exam:

• 90 questions (multiple choice and performance-based)
• 90 minutes duration
• Passing Score: 750 (scale 100-900)

Domains:
• General Security Concepts - 12%
• Threats, Vulnerabilities, and Mitigations - 22%
• Security Architecture - 18%
• Security Operations - 28%
• Security Program Management and Oversight - 20%
```

---

## 🎯 Quiz Functions

### 6. `quiz_me(num_questions)`
**Purpose:** Take a practice quiz

**Voice Command:**
```
"Quiz me with 3 questions"
"Give me 5 quiz questions"
```

---

### 7. `check_answer(answer)`
**Purpose:** Check your quiz answers

**Voice Command:**
```
"My answer is B"
"Check my answers: A, C, B"
```

---

## 📊 Progress Functions

### 8. `get_progress()`
**Purpose:** See your study statistics

**Voice Command:**
```
"Show my progress"
"What's my progress?"
```

---

### 9. `get_study_tips()`
**Purpose:** Get exam study tips

**Voice Command:**
```
"Give me study tips"
"What are your study tips?"
```

---

## 🎓 Comparison: Which Function to Use?

| Situation | Best Function | Why |
|-----------|---------------|-----|
| Quick lookup | `explain_topic()` | Fast, structured info |
| Learning new concept | `teach_lesson()` | Interactive, conversational |
| Polished presentation | `deliver_scripted_lesson()` | Pre-written, professional |
| Browse available content | `list_topics()` | See what's available |
| Test knowledge | `quiz_me()` | Active practice |
| Track learning | `get_progress()` | Monitor improvement |

---

## 🚀 Usage Examples

### Studying a New Topic
```
1. "List topics in domain 1"                    (Browse)
2. "Explain security controls from domain 1"    (Quick overview)
3. "Teach me about security controls"           (Deep dive)
4. "Quiz me with 2 questions"                   (Test yourself)
```

### Using Scripted Content
```
1. "List topics in domain 1"
2. "Deliver scripted lesson on security controls from domain 1"
3. (Listen to polished lesson)
4. "Quiz me with 3 questions"
```

### Comprehensive Study Session
```
1. "Give me an exam overview"                   (Big picture)
2. "List topics in domain 1"                    (See content)
3. "Teach me about security controls"           (Learn)
4. "Deliver scripted lesson on security controls" (Reinforce)
5. "Quiz me with 5 questions"                   (Practice)
6. "Show my progress"                           (Track)
```

---

## 📝 Notes

- All functions work with voice commands when the agent is running
- Domain numbers: `domain_1` through `domain_5`
- Topic names use underscores: `security_controls`, `fundamental_concepts`
- Scripted lessons are optional - not all topics have them yet
- The agent will guide you if you request unavailable content

---

## Current Scripted Lessons

✅ **Available:**
- domain_1 / security_controls

⏳ **Coming Soon:**
- Additional topics as scripts are added

To add more, see: `SCRIPTED_LESSONS_GUIDE.md`
