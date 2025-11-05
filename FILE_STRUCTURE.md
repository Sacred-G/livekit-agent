# Project File Structure

## ✅ Organized File Structure

```
livekit-agent/
│
├── 📄 Core Agent Files
│   ├── security_plus_agent.py         # Main Security+ teaching agent
│   ├── livekit_basic_agent.py          # Basic LiveKit agent template
│   ├── livekit_mcp_agent.py            # MCP-enabled agent
│   └── security_plus_knowledge_base.py # Practice questions ONLY (cleaned up)
│
├── 📚 Documentation (docs/)
│   ├── INDEX.md                        # Documentation index (START HERE)
│   ├── SECURITY_PLUS_README.md         # Security+ agent overview
│   ├── KNOWLEDGE_BASE_INTEGRATION.md   # Knowledge base setup guide
│   ├── INTEGRATION_SUMMARY.md          # Integration summary
│   ├── SCRIPTED_LESSONS_GUIDE.md       # Scripted lesson guide
│   ├── LESSON_FUNCTIONS_QUICK_REFERENCE.md  # Function reference
│   ├── TEST_COMMANDS.md                # Test commands
│   ├── CLAUDE.md                       # Development notes
│   ├── exam_outline.md                 # Security+ exam outline
│   └── CompTIA-Security-Plus-SY0-701.pdf  # Official exam PDF
│
├── 🧪 Tests (tests/)
│   ├── test_knowledge_base.py          # Test knowledge base integration
│   ├── test_scripted_lesson.py         # Test scripted lessons
│   └── verify_kb.py                    # Quick verification script
│
├── 📖 Knowledge Base (domains/)
│   ├── __init__.py                     # Exports ALL_DOMAINS
│   ├── README.md                       # Domain structure documentation
│   ├── LESSON_TEMPLATE.py              # Template for new lessons
│   ├── domain_1/
│   │   ├── __init__.py
│   │   ├── knowledge.py                # General Security Concepts (12%)
│   │   └── lessons/
│   │       ├── lesson1_security_controls.py
│   │       └── lesson2_malware_types.py
│   ├── domain_2/
│   │   ├── __init__.py
│   │   ├── knowledge.py                # Threats, Vulnerabilities (22%)
│   │   └── lessons/
│   ├── domain_3/
│   │   ├── __init__.py
│   │   ├── knowledge.py                # Security Architecture (18%)
│   │   └── lessons/
│   ├── domain_4/
│   │   ├── __init__.py
│   │   ├── knowledge.py                # Security Operations (28%)
│   │   └── lessons/
│   └── domain_5/
│       ├── __init__.py
│       ├── knowledge.py                # Security Program Management (20%)
│       └── lessons/
│
├── 📝 Legacy Lessons (lessons/)
│   └── lesson1.py                      # Original lesson (now integrated)
│
├── ⚙️ Configuration
│   ├── .env                            # Environment variables (API keys)
│   ├── .gitignore                      # Git ignore rules
│   ├── pyproject.toml                  # Python project configuration
│   ├── uv.lock                         # UV dependency lock file
│   └── README.md                       # Main project README
│
└── 🔧 Other
    ├── .venv/                          # Virtual environment
    ├── __pycache__/                    # Python cache
    └── .git/                           # Git repository
```

## 📊 File Organization Summary

### What Changed

✅ **Documentation consolidated** - All `.md` files moved to `docs/` folder  
✅ **Tests organized** - All test scripts moved to `tests/` folder  
✅ **Knowledge base cleaned** - `security_plus_knowledge_base.py` now only contains PRACTICE_QUESTIONS  
✅ **Structure documented** - Created `docs/INDEX.md` for easy navigation  

### What's Where

| What You Need | Where to Find It |
|---------------|------------------|
| Start here | `docs/INDEX.md` |
| Run the agent | `security_plus_agent.py` |
| Add knowledge | `domains/domain_X/knowledge.py` |
| Add questions | `security_plus_knowledge_base.py` |
| Test setup | `tests/test_knowledge_base.py` |
| All documentation | `docs/` folder |

### Key Points

1. **`security_plus_knowledge_base.py`** is STILL USED but only for `PRACTICE_QUESTIONS`
2. **Knowledge base** comes from `domains/` package (ALL_DOMAINS)
3. **All documentation** is now in `docs/` folder
4. **All tests** are now in `tests/` folder

## 🚀 Quick Start

1. **Read documentation**: Start with `docs/INDEX.md`
2. **Run agent**: `python security_plus_agent.py dev`
3. **Test setup**: `uv run python tests/test_knowledge_base.py`
4. **Add content**: Edit files in `domains/` folder

## 📝 Notes

- Root folder now only contains essential files (agent scripts, config, README)
- Documentation is centralized for easy access
- Tests are separated for clean organization
- Knowledge base is modular by domain
