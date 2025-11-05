"""
Lesson Template
===============
Copy this template when creating new lessons for any domain.

Instructions:
1. Copy this file to the appropriate domain's lessons folder
2. Rename it following the pattern: lessonX_topic_name.py
3. Update the header with domain and topic information
4. Fill in the LESSON_SCRIPT with your teaching content
5. Use the voice cues as shown below

Voice Cues Reference:
- [break:1s] or [break:2s] - Pause for X seconds
- [checkpoint] - Natural pause for understanding check
- [exam] - Mark exam-specific tips
- [recap] - Signal summary section
- [emph] and [/emph] - Emphasize text
- [slow] and [/slow] - Speak slowly for definitions
"""

LESSON_METADATA = {
    "domain": "domain_X",  # e.g., domain_1, domain_2, etc.
    "topic": "topic_name",  # e.g., malware, cryptography, etc.
    "lesson_number": 1,
    "title": "Lesson Title Here",
    "duration_minutes": 15,  # Estimated duration
    "difficulty": "beginner",  # beginner, intermediate, advanced
    "prerequisites": [],  # List any prerequisite lessons
}

LESSON_SCRIPT = """
[Your lesson introduction here - greet the class naturally]

[break:1s]

[Main teaching content - break into digestible sections]

[break:1.5s]

[Key concept explanation with examples]

[checkpoint]

[Another major point or concept]

[break:1s]

[Real-world scenario or story]

[exam]
For the exam, remember:
- Key point 1
- Key point 2
- Key point 3

[recap]
To summarize:
[Your summary points]

[break:2s]

[Closing - invite questions]
"""

# Optional: Define key terms covered in this lesson
KEY_TERMS = [
    "term1: definition",
    "term2: definition",
    "term3: definition",
]

# Optional: Related exam objectives
EXAM_OBJECTIVES = [
    "1.1 - Objective description",
    "1.2 - Objective description",
]