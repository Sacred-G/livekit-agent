# Security+ Domains Structure

This directory contains the organized knowledge base and lesson scripts for the CompTIA Security+ (SY0-701) exam, structured by domain.

## Directory Structure

```
domains/
├── __init__.py                    # Main package with consolidated knowledge
├── LESSON_TEMPLATE.py             # Template for creating new lessons
├── domain_1/                      # General Security Concepts (12%)
│   ├── __init__.py
│   ├── knowledge.py               # Domain 1 knowledge base
│   └── lessons/
│       ├── lesson1_security_controls.py
│       └── lesson2_malware_types.py
├── domain_2/                      # Threats, Vulnerabilities, and Mitigations (22%)
│   ├── __init__.py
│   ├── knowledge.py
│   └── lessons/
├── domain_3/                      # Security Architecture (18%)
│   ├── __init__.py
│   ├── knowledge.py
│   └── lessons/
├── domain_4/                      # Security Operations (28%)
│   ├── __init__.py
│   ├── knowledge.py
│   └── lessons/
└── domain_5/                      # Security Program Management and Oversight (20%)
    ├── __init__.py
    ├── knowledge.py
    └── lessons/
```

## Domain Overview

### Domain 1: General Security Concepts (12%)
**Location:** `domain_1/`
**Official Objectives:**
- Security controls (technical, managerial, operational, physical)
- Fundamental security concepts (CIA Triad, non-repudiation, AAA)
- Change management processes
- Cryptographic solutions (PKI, encryption, hashing, certificates)

### Domain 2: Threats, Vulnerabilities, and Mitigations (22%)
**Location:** `domain_2/`
**Official Objectives:**
- Threat actors and motivations
- Threat vectors and attack surfaces
- Vulnerability types
- Indicators of malicious activity (malware, attacks)
- Mitigation techniques

### Domain 3: Security Architecture (18%)
**Location:** `domain_3/`
**Official Objectives:**
- Security implications of architecture models (cloud, hybrid, IoT, ICS/SCADA)
- Security principles for enterprise infrastructure
- Data protection methods
- Resilience and recovery (high availability, backups, disaster recovery)

### Domain 4: Security Operations (28%)
**Location:** `domain_4/`
**Official Objectives:**
- Security techniques (hardening, wireless security, application security)
- Asset management
- Vulnerability management
- Security alerting and monitoring
- Identity and access management
- Modifying enterprise capabilities (automation, incident response)
- Using data sources (logs, vulnerability scans, packet captures)

### Domain 5: Security Program Management and Oversight (20%)
**Location:** `domain_5/`
**Official Objectives:**
- Security governance (policies, standards, procedures)
- Risk management (assessment, BIA, RTO/RPO)
- Third-party risk management
- Compliance and monitoring
- Audits and assessments
- Security awareness and training

## Usage

### Importing Knowledge Bases

```python
# Import all domains
from domains import ALL_DOMAINS

# Import specific domain
from domains.domain_1 import DOMAIN_1_KNOWLEDGE

# Access domain data
domain_1 = ALL_DOMAINS["domain_1"]
print(domain_1["name"])
print(domain_1["weight"])
```

### Creating New Lessons

1. Copy the `LESSON_TEMPLATE.py` file
2. Place it in the appropriate domain's `lessons/` folder
3. Rename following pattern: `lessonX_topic_name.py`
4. Fill in the template with your content

Example:
```bash
cp LESSON_TEMPLATE.py domain_1/lessons/lesson3_social_engineering.py
```

### Lesson Script Format

Each lesson script should include:

```python
LESSON_METADATA = {
    "domain": "domain_1",
    "topic": "malware",
    "lesson_number": 2,
    "title": "Understanding Malware Types",
    "duration_minutes": 15,
    "difficulty": "beginner",
    "prerequisites": [],
}

LESSON_SCRIPT = """
[Your lesson content with voice cues]
"""
```

### Voice Cues

Use these cues in lesson scripts for natural teaching flow:

- `[break:1s]` or `[break:2s]` - Pause for reflection
- `[checkpoint]` - Natural pause to check understanding
- `[exam]` - Signal exam-specific tips
- `[recap]` - Mark summary sections
- `[emph]...[/emph]` - Emphasize important text
- `[slow]...[/slow]` - Speak slowly for definitions

## Knowledge Base Structure

Each `knowledge.py` file contains:

```python
DOMAIN_X_KNOWLEDGE = {
    "name": "Domain Name",
    "weight": "XX%",
    "topics": {
        "topic_name": {
            "description": "Brief description",
            "types": [...],        # or "concepts", "phases", etc.
            "key_points": [...]
        }
    }
}
```

## Adding New Content

### Adding a New Topic to a Domain

1. Open the domain's `knowledge.py` file
2. Add a new topic entry under `"topics"`
3. Follow the existing structure
4. Create corresponding lesson files

### Adding a New Lesson

1. Use `LESSON_TEMPLATE.py` as starting point
2. Update metadata (domain, topic, lesson number)
3. Write the lesson script with natural teaching flow
4. Include voice cues for pacing
5. Save in appropriate domain's `lessons/` folder

### Lesson Naming Convention

- Format: `lessonX_topic_name.py`
- X = lesson number (sequential within domain)
- topic_name = descriptive snake_case name
- Example: `lesson3_incident_response_phases.py`

## Best Practices

1. **Keep lessons focused** - Each lesson should cover one specific topic
2. **Use realistic examples** - Include real-world scenarios
3. **Add exam connections** - Mark exam-relevant content with `[exam]` cue
4. **Vary teaching style** - Use different teaching flows (story-first, example-first, etc.)
5. **Include checkpoints** - Add natural pauses for comprehension
6. **Update knowledge bases** - Keep knowledge.py files synchronized with lessons

## Integration with Agent

The Security+ agent can load domains dynamically:

```python
from domains import ALL_DOMAINS

# Access any domain
for domain_id, domain_data in ALL_DOMAINS.items():
    print(f"{domain_data['name']}: {domain_data['weight']}")
```

## Maintenance

- Review and update content regularly
- Add new lessons as exam objectives change
- Keep knowledge bases aligned with current Security+ (SY0-701) exam
- Test lesson scripts for natural flow and pacing

## Contributing

When adding new content:
1. Follow the existing structure
2. Use the lesson template
3. Include metadata and voice cues
4. Test lesson flow
5. Update this README if needed

---

**Last Updated:** 2025-01-05
**Exam Version:** CompTIA Security+ SY0-701