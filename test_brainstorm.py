#!/usr/bin/env python3
"""
Test script to demonstrate the improved brainstorming functionality
"""

from smart_writer import MyWritingAssistant

def test_brainstorm():
    print("🧪 Testing improved brainstorming functionality...")
    assistant = MyWritingAssistant()
    
    # Test with the same topic that had poor results
    topic = "productivity hacks on a mac"
    print(f"\n🎯 Testing brainstorm for: '{topic}'")
    
    ideas = assistant.brainstorm_ideas(topic)
    
    print(f"\n📝 Generated ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"\n{i}. {idea}")
        print("-" * 50)

if __name__ == "__main__":
    test_brainstorm()
