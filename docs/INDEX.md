# Documentation Index

All documentation for the Security+ Teaching Agent.

## 📚 Quick Start

- **[README.md](../README.md)** - Main project README (in root folder)
- **[SECURITY_PLUS_README.md](SECURITY_PLUS_README.md)** - Security+ agent overview and features

## 🔧 Setup & Integration

- **[KNOWLEDGE_BASE_INTEGRATION.md](KNOWLEDGE_BASE_INTEGRATION.md)** - How the knowledge base is connected
- **[INTEGRATION_SUMMARY.md](INTEGRATION_SUMMARY.md)** - Summary of recent integrations
- **[TEST_COMMANDS.md](TEST_COMMANDS.md)** - Quick test commands for verification

## 📖 Feature Guides

- **[SCRIPTED_LESSONS_GUIDE.md](SCRIPTED_LESSONS_GUIDE.md)** - How to use and add scripted lessons
- **[LESSON_FUNCTIONS_QUICK_REFERENCE.md](LESSON_FUNCTIONS_QUICK_REFERENCE.md)** - All available lesson functions

## 📝 Reference Materials

- **[exam_outline.md](exam_outline.md)** - CompTIA Security+ SY0-701 exam outline
- **[CompTIA-Security-Plus-SY0-701.pdf](CompTIA-Security-Plus-SY0-701.pdf)** - Official exam PDF
- **[CLAUDE.md](CLAUDE.md)** - Development notes and Claude instructions

## 📁 File Structure

```
livekit-agent/
├── README.md                          # Main project README
├── security_plus_agent.py             # Main agent file
├── security_plus_knowledge_base.py    # Practice questions only
├── docs/                              # All documentation (THIS FOLDER)
│   ├── INDEX.md                       # This file
│   ├── SECURITY_PLUS_README.md
│   ├── KNOWLEDGE_BASE_INTEGRATION.md
│   ├── INTEGRATION_SUMMARY.md
│   ├── SCRIPTED_LESSONS_GUIDE.md
│   ├── LESSON_FUNCTIONS_QUICK_REFERENCE.md
│   ├── TEST_COMMANDS.md
│   ├── CLAUDE.md
│   ├── exam_outline.md
│   └── CompTIA-Security-Plus-SY0-701.pdf
├── domains/                           # Knowledge base by domain
│   ├── __init__.py                    # Exports ALL_DOMAINS
│   ├── domain_1/
│   │   ├── __init__.py
│   │   ├── knowledge.py               # Domain 1 knowledge
│   │   └── lessons/                   # Domain 1 lesson scripts
│   ├── domain_2/
│   │   ├── __init__.py
│   │   └── knowledge.py               # Domain 2 knowledge
│   ├── domain_3/
│   ├── domain_4/
│   └── domain_5/
├── tests/                             # Test scripts
│   ├── test_knowledge_base.py
│   ├── test_scripted_lesson.py
│   └── verify_kb.py
└── lessons/                           # Original lesson files
    └── lesson1.py
```

## 🎯 Quick Links by Task

### I want to...

**Run the agent:**
- See [SECURITY_PLUS_README.md](SECURITY_PLUS_README.md#running-the-agent)

**Test the knowledge base:**
- See [TEST_COMMANDS.md](TEST_COMMANDS.md)
- Run: `uv run python tests/test_knowledge_base.py`

**Add a scripted lesson:**
- See [SCRIPTED_LESSONS_GUIDE.md](SCRIPTED_LESSONS_GUIDE.md#how-to-add-more-scripted-lessons)

**Understand available functions:**
- See [LESSON_FUNCTIONS_QUICK_REFERENCE.md](LESSON_FUNCTIONS_QUICK_REFERENCE.md)

**Add more topics to the knowledge base:**
- Edit `domains/domain_X/knowledge.py` files
- See [KNOWLEDGE_BASE_INTEGRATION.md](KNOWLEDGE_BASE_INTEGRATION.md)

**Add more practice questions:**
- Edit `security_plus_knowledge_base.py` (PRACTICE_QUESTIONS list)

## 📊 Project Status

✅ Knowledge base: **Connected** (using comprehensive domains package)  
✅ Scripted lessons: **Functional** (domain_1/security_controls available)  
✅ Practice quizzes: **Working** (3 questions, expandable)  
✅ Voice functions: **All operational** (9 functions available)  
✅ Documentation: **Organized** (in docs folder)

## 🔄 Recent Changes

- Moved all documentation to `docs/` folder
- Moved all test scripts to `tests/` folder
- Cleaned up `security_plus_knowledge_base.py` (now only contains PRACTICE_QUESTIONS)
- Integrated comprehensive domain knowledge from `domains/` package
- Added scripted lesson support for pre-written content

## 📧 Need Help?

Refer to the specific guide for your task above, or check the main [README.md](../README.md).
