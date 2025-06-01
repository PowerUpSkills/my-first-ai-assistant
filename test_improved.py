#!/usr/bin/env python3
"""
Test the improved writing assistant
"""

from smart_writer_improved import ImprovedWritingAssistant

def test_both_approaches():
    print("🧪 Testing improved writing assistant...")
    assistant = ImprovedWritingAssistant()
    
    topic = "productivity hacks on a mac"
    
    print(f"\n🤖 AI-Generated Ideas for '{topic}':")
    print("=" * 50)
    ai_ideas = assistant.brainstorm_ideas(topic)
    for i, idea in enumerate(ai_ideas, 1):
        print(f"{i}. {idea}")
    
    print(f"\n📚 Curated Tips for '{topic}':")
    print("=" * 50)
    curated_tips = assistant.get_curated_tips(topic)
    for i, tip in enumerate(curated_tips, 1):
        print(f"{i}. {tip}")
    
    print("\n💡 Comparison:")
    print("- AI ideas may be creative but less reliable")
    print("- Curated tips are accurate and actionable")
    print("- Best approach: Combine both for variety and quality")

if __name__ == "__main__":
    test_both_approaches()
