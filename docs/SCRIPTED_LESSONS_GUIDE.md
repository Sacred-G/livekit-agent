# Scripted Lessons Guide

## Overview

The Security+ agent now supports **pre-written scripted lessons** that can be delivered verbatim. This allows you to create polished, rehearsed lesson content that the agent will read exactly as written.

## ✅ What's Been Set Up

### 1. Scripted Lesson Added
The lesson script from `lessons/lesson1.py` has been integrated into the knowledge base:

**Location:** `domains/domain_1/knowledge.py`  
**Topic:** `security_controls`  
**Field:** `scripted_lesson`

### 2. New Agent Function
A new function `deliver_scripted_lesson()` has been added to the agent to retrieve and deliver scripted lessons.

## How to Use

### Voice Commands

When the agent is running, you can request scripted lessons with:

```
"Deliver the scripted lesson on security controls from domain 1"
"Give me the scripted lesson for security controls"
"Read the security controls script from domain 1"
```

### Function Call

The agent function signature:
```python
deliver_scripted_lesson(domain: str, topic: str) -> str
```

**Example:**
```python
deliver_scripted_lesson(domain='domain_1', topic='security_controls')
```

### Expected Output

The agent will deliver:
```
📚 Scripted Lesson: Security Controls

Domain: General Security Concepts

Let's be real, no prevention is ever perfect. So, what happens if an 
attacker gets past that first line? Well, that's where detective controls 
come in. Their job isn't to stop the incident, but to identify it and 
sound the alarm...

[Full scripted content continues...]
```

## Current Scripted Lessons

| Domain | Topic | Available |
|--------|-------|-----------|
| domain_1 | security_controls | ✅ Yes |
| domain_1 | fundamental_concepts | ❌ No |
| domain_1 | cryptography | ❌ No |
| domain_2+ | (all topics) | ❌ No |

## How to Add More Scripted Lessons

### Step 1: Add to Domain Knowledge

Edit the relevant `domains/domain_X/knowledge.py` file and add a `scripted_lesson` field to any topic:

```python
"your_topic": {
    "description": "Topic description",
    "types": [...],
    "key_points": [...],
    "scripted_lesson": """Your complete lesson script goes here.
    
    Write it exactly as you want the agent to deliver it.
    
    Include natural pauses, emphasis, and flow.
    
    The agent will read this verbatim.""",
},
```

### Step 2: Test the Lesson

Run the test script:
```bash
uv run python test_scripted_lesson.py
```

### Step 3: Use in Agent

Start the agent and request the scripted lesson by name.

## Scripted vs Dynamic Lessons

The agent now has three ways to deliver lessons:

### 1. `explain_topic(domain, topic)`
- **Type:** Dynamic
- **Content:** Pulls from knowledge base fields (categories, types, key_points)
- **Format:** Structured bullet points
- **Use when:** You want comprehensive reference information

### 2. `teach_lesson(domain, topic)`
- **Type:** Dynamic + Conversational
- **Content:** Uses knowledge base + teaching language
- **Format:** Classroom-style with natural flow
- **Use when:** You want an interactive teaching experience

### 3. `deliver_scripted_lesson(domain, topic)` 🆕
- **Type:** Scripted (Pre-written)
- **Content:** Reads exact text from `scripted_lesson` field
- **Format:** Exactly as written in the script
- **Use when:** You want polished, rehearsed content delivered verbatim

## Benefits of Scripted Lessons

✅ **Consistency** - Every student hears the exact same content  
✅ **Polish** - Pre-written and carefully crafted for clarity  
✅ **Control** - You control every word and emphasis  
✅ **Professional** - Sounds like a prepared lecture  
✅ **Reusable** - Script once, deliver many times

## Lesson Script Format Tips

When writing scripted lessons:

1. **Write for speaking** - Use conversational language
2. **Use natural pauses** - Line breaks indicate pacing
3. **Include examples** - Make concepts concrete
4. **Build progressively** - Start simple, add complexity
5. **End with reflection** - Leave students thinking
6. **Keep it focused** - 3-5 minutes of content maximum

## Testing Your Scripted Lesson

```bash
# Test that lesson is accessible
uv run python test_scripted_lesson.py

# Test with the agent
python security_plus_agent.py dev
# Then say: "Deliver scripted lesson on security controls from domain 1"
```

## Example: Converting lesson1.py Scripts

The original `lessons/lesson1.py` format was:
```python
self.knowledge_base["domain_1"]["lesson"] = """..."""
```

This has been converted to:
```python
"security_controls": {
    # ... other fields ...
    "scripted_lesson": """...""",
}
```

To convert more lesson files:
1. Find the topic the lesson covers
2. Add `scripted_lesson` field to that topic in the domain knowledge
3. Copy the lesson text into that field

## File Structure

```
livekit-agent/
├── domains/
│   ├── domain_1/
│   │   ├── knowledge.py          ← Scripted lessons stored here
│   │   └── lessons/              ← Optional: additional lesson files
│   ├── domain_2/
│   │   └── knowledge.py
│   └── ...
├── lessons/
│   └── lesson1.py                ← Original source (can be archived)
├── security_plus_agent.py        ← Uses deliver_scripted_lesson()
└── test_scripted_lesson.py       ← Test script
```

## Status

✅ Scripted lesson framework: **COMPLETE**  
✅ Domain 1 / security_controls: **COMPLETE**  
⏳ Additional scripted lessons: **Available to add**

## Next Steps

1. Test the existing scripted lesson
2. Add more scripted lessons to other topics
3. Create lesson scripts for domains 2-5
4. Combine with dynamic teaching for best experience
