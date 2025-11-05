#!/usr/bin/env python3

print("Script is running...")

import asyncio
from livekit.agents import AgentSession
from security_plus_agent import SecurityPlusTeacher

async def test_quiz():
    print("Starting quiz test...")
    
    # Create a mock context
    class MockContext:
        def __init__(self):
            self.metadata = {}
        
        def store_metadata(self, key, value):
            self.metadata[key] = value
            print(f"Stored metadata: {key} = {value}")
            
        def get_metadata(self, key):
            value = self.metadata.get(key)
            print(f"Got metadata: {key} = {value}")
            return value
    
    # Initialize teacher
    print("Initializing teacher...")
    teacher = SecurityPlusTeacher()
    print(f"Teacher has {len(teacher.practice_questions)} practice questions")
    
    # Create mock context
    context = MockContext()
    
    # Test quiz function
    try:
        print("Calling quiz_me function...")
        result = await teacher.quiz_me(context, 2)
        print("Quiz function result:")
        print(result)
        print("\nQuiz stored in metadata:")
        print(context.get_metadata("current_quiz"))
    except Exception as e:
        print(f"Error in quiz function: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_quiz())
