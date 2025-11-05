#!/usr/bin/env python3

from security_plus_knowledge_base import DOMAIN_PRACTICE_QUESTIONS, PRACTICE_QUESTIONS

print("Security+ Practice Questions Summary")
print("=" * 40)

total_questions = len(PRACTICE_QUESTIONS)
print(f"Total questions available: {total_questions}")
print()

for domain, questions in DOMAIN_PRACTICE_QUESTIONS.items():
    print(f"{domain}: {len(questions)} questions")

print()
print("Sample question from each domain:")
for domain, questions in DOMAIN_PRACTICE_QUESTIONS.items():
    if questions:
        print(f"\n{domain}:")
        print(f"  Q: {questions[0]['question']}")
        print(f"  A: {questions[0]['correct']}")
