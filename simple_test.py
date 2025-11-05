#!/usr/bin/env python3

# Test the basic functionality without LiveKit dependencies
print("Testing basic quiz functionality...")

try:
    # Test importing PRACTICE_QUESTIONS
    from security_plus_knowledge_base import PRACTICE_QUESTIONS
    print(f"✓ Successfully imported {len(PRACTICE_QUESTIONS)} practice questions")
    
    # Test the questions structure
    for i, q in enumerate(PRACTICE_QUESTIONS):
        print(f"Question {i+1}: {q['question']}")
        print(f"Options: {q['options']}")
        print(f"Correct: {q['correct']}")
        print("---")
    
    # Test random sampling
    import random
    sampled = random.sample(PRACTICE_QUESTIONS, 2)
    print(f"✓ Successfully sampled {len(sampled)} questions")
    
    print("All basic tests passed!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
