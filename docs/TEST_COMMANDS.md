# Quick Test Commands for Knowledge Base Verification

## Voice Commands to Test (When Agent is Running)

Once you start the agent with `python security_plus_agent.py dev`, try these:

### 1. Browse Available Topics
```
"List topics in domain 1"
"List topics in domain 2"
"List topics in domain 4"
```

**Expected:** You should see comprehensive topic lists for each domain.

### 2. Get Detailed Explanations
```
"Explain security controls from domain 1"
"Explain cryptography from domain 1"
"Explain threat actors from domain 2"
"Explain security techniques from domain 4"
```

**Expected:** Detailed explanations with multiple subcategories (categories, types, key points, etc.)

### 3. Request Structured Lessons
```
"Teach me about cryptography from domain 1"
"Teach me about incident response from domain 4"
"Teach me about risk management from domain 5"
```

**Expected:** Classroom-style teaching format with multiple sections.

### 4. Check Exam Overview
```
"Give me an exam overview"
"What's the exam structure?"
```

**Expected:** Shows all 5 domains with correct names and weights:
- General Security Concepts (12%)
- Threats, Vulnerabilities, and Mitigations (22%)
- Security Architecture (18%)
- Security Operations (28%)
- Security Program Management and Oversight (20%)

## Python Commands to Verify (Without Running Agent)

### Quick Check
```bash
cd c:\Users\jfc-t\Dev\voice-app\livekit-agent
uv run python verify_kb.py
```

### Inline Verification
```bash
uv run python -c "from domains import ALL_DOMAINS; [print(f'{k}: {v[\"name\"]} - {len(v[\"topics\"])} topics') for k,v in ALL_DOMAINS.items()]"
```

### Test Specific Topic
```bash
uv run python -c "from domains import ALL_DOMAINS; sec = ALL_DOMAINS['domain_1']['topics']['security_controls']; print(f'Description: {sec[\"description\"]}'); print(f'Fields: {list(sec.keys())}'); print(f'Key points: {len(sec[\"key_points\"])}')"
```

## Expected Knowledge Base Stats

- **Total Domains:** 5
- **Domain 1 Topics:** 7 (security_controls, fundamental_concepts, zero_trust, physical_security, deception_technology, change_management, cryptography)
- **Domain 2 Topics:** 6 (threat_actors, threat_vectors, vulnerabilities, indicators_of_malicious_activity, threat_intelligence, mitigation_techniques)
- **Domain 3 Topics:** 4 (architecture_models, security_principles, data_protection, resilience_and_recovery)
- **Domain 4 Topics:** 7 (security_techniques, asset_management, vulnerability_management, alerting_and_monitoring, identity_access_management, automation_orchestration, data_sources)
- **Domain 5 Topics:** 6 (security_governance, risk_management, third_party_risk, compliance_and_audits, security_awareness, types_of_agreements)

## Troubleshooting

### If topics seem limited or basic:
❌ Agent might still be using old knowledge base
✅ Check `security_plus_agent.py` line 14: Should show `from domains import ALL_DOMAINS`
✅ Check `security_plus_agent.py` line 127: Should show `self.knowledge_base = ALL_DOMAINS`

### If import fails:
❌ Domains package not found
✅ Check `domains/__init__.py` exists
✅ Check all `domains/domain_X/knowledge.py` files exist
✅ Run from `livekit-agent` directory

### If agent won't start:
❌ Missing environment variables
✅ Check `.env` file has required API keys (OpenAI, Deepgram, LiveKit)
