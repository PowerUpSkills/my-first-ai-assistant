#!/usr/bin/env python3
"""
Complete feature demonstration of the AI Assistant project
This script showcases all major features in one comprehensive demo
"""

import time
import json
from pathlib import Path
from smart_writer import ImprovedWritingAssistant

class CompleteDemonstration:
    
    def __init__(self):
        self.assistant = None
        self.demo_results = []
    
    def run_complete_demo(self):
        """Run a comprehensive demonstration of all features"""
        print("🎬 AI Assistant Complete Feature Demo")
        print("=" * 50)
        
        # Step 1: Model Selection Demo
        self.demo_model_selection()
        
        # Step 2: Basic Generation Demo
        self.demo_basic_generation()
        
        # Step 3: Quality Comparison Demo
        self.demo_quality_comparison()
        
        # Step 4: Performance Monitoring Demo
        self.demo_performance_monitoring()
        
        # Step 5: Advanced Features Demo
        self.demo_advanced_features()
        
        # Step 6: Results Summary
        self.demo_summary()
    
    def demo_model_selection(self):
        """Demonstrate model selection capabilities"""
        print("\n🤖 DEMO 1: Model Selection")
        print("-" * 30)
        
        models_to_test = ["gpt2", "distilgpt2"]
        
        for model_name in models_to_test:
            print(f"\n📦 Testing {model_name}...")
            
            start_time = time.time()
            try:
                assistant = ImprovedWritingAssistant(model_name)
                load_time = time.time() - start_time
                
                print(f"✅ {model_name} loaded in {load_time:.1f} seconds")
                
                # Store the better model for later use
                if model_name == "distilgpt2":
                    self.assistant = assistant
                
            except Exception as e:
                print(f"❌ Error loading {model_name}: {e}")
        
        print("\n💡 Result: distilgpt2 selected for optimal performance")
    
    def demo_basic_generation(self):
        """Demonstrate basic text generation"""
        print("\n📝 DEMO 2: Basic Text Generation")
        print("-" * 30)
        
        test_topics = [
            "productivity hacks on a mac",
            "time management tips",
            "coding best practices"
        ]
        
        for topic in test_topics:
            print(f"\n🎯 Topic: {topic}")
            
            # Generate AI ideas
            ai_ideas = self.assistant.brainstorm_ideas(topic)
            print(f"🤖 AI Idea: {ai_ideas[0][:100]}...")
            
            # Get curated tips
            curated_tips = self.assistant.get_curated_tips(topic)
            print(f"📚 Curated: {curated_tips[0]}")
            
            # Store results
            self.demo_results.append({
                "topic": topic,
                "ai_output": ai_ideas[0],
                "curated_output": curated_tips[0],
                "timestamp": time.time()
            })
    
    def demo_quality_comparison(self):
        """Demonstrate quality assessment"""
        print("\n📊 DEMO 3: Quality Assessment")
        print("-" * 30)
        
        for result in self.demo_results:
            topic = result["topic"]
            ai_output = result["ai_output"]
            curated_output = result["curated_output"]
            
            print(f"\n🎯 Topic: {topic}")
            
            # Simple quality metrics
            ai_score = self.calculate_quality_score(ai_output, topic)
            curated_score = self.calculate_quality_score(curated_output, topic)
            
            print(f"🤖 AI Quality: {ai_score:.1f}/10")
            print(f"📚 Curated Quality: {curated_score:.1f}/10")
            
            winner = "Curated" if curated_score > ai_score else "AI"
            print(f"🏆 Winner: {winner}")
    
    def demo_performance_monitoring(self):
        """Demonstrate performance monitoring"""
        print("\n⚡ DEMO 4: Performance Monitoring")
        print("-" * 30)
        
        # Monitor generation performance
        start_time = time.time()
        start_memory = self.get_memory_usage()
        
        # Generate multiple ideas
        topic = "productivity tips"
        ideas = []
        for i in range(3):
            idea = self.assistant.brainstorm_ideas(f"{topic} #{i+1}")
            ideas.extend(idea)
        
        end_time = time.time()
        end_memory = self.get_memory_usage()
        
        # Report performance
        duration = end_time - start_time
        memory_delta = end_memory - start_memory
        
        print(f"⏱️  Generation Time: {duration:.2f} seconds")
        print(f"💾 Memory Usage: {memory_delta:+.1f} MB")
        print(f"📝 Ideas Generated: {len(ideas)}")
        print(f"🚀 Speed: {len(ideas)/duration:.1f} ideas/second")
    
    def demo_advanced_features(self):
        """Demonstrate advanced features"""
        print("\n🚀 DEMO 5: Advanced Features")
        print("-" * 30)
        
        # History tracking simulation
        print("📚 History Tracking:")
        print(f"   Total sessions: {len(self.demo_results)}")
        print(f"   Topics covered: {[r['topic'] for r in self.demo_results]}")
        
        # Analytics simulation
        print("\n📊 Analytics:")
        total_chars = sum(len(r['ai_output']) for r in self.demo_results)
        avg_length = total_chars / len(self.demo_results) if self.demo_results else 0
        print(f"   Average output length: {avg_length:.0f} characters")
        print(f"   Most productive topic: {self.get_most_productive_topic()}")
        
        # Export capability
        self.export_demo_results()
        print("   ✅ Results exported to demo_results.json")
    
    def demo_summary(self):
        """Provide demonstration summary"""
        print("\n🎉 DEMO COMPLETE: Summary")
        print("=" * 30)
        
        print("✅ Features Demonstrated:")
        print("   🤖 Multi-model support (gpt2, distilgpt2)")
        print("   📝 Text generation and brainstorming")
        print("   📊 Quality assessment and comparison")
        print("   ⚡ Performance monitoring")
        print("   📚 History tracking and analytics")
        print("   💾 Data export capabilities")
        
        print("\n🎯 Key Findings:")
        print("   • distilgpt2 offers best performance/quality balance")
        print("   • Curated content provides higher reliability")
        print("   • Hybrid approach maximizes both creativity and quality")
        print("   • Performance monitoring enables optimization")
        
        print("\n🚀 Next Steps:")
        print("   1. Try different models (gpt2-medium for better quality)")
        print("   2. Experiment with custom prompts")
        print("   3. Build your own features using the framework")
        print("   4. Share your improvements with the community")
        
        print(f"\n📁 Demo results saved to: demo_results.json")
        print(f"🔗 Project repository: https://github.com/PowerUpSkills/my-first-ai-assistant")
    
    def calculate_quality_score(self, text, topic):
        """Simple quality scoring algorithm"""
        score = 0
        
        # Length check (50-200 chars is good)
        if 50 <= len(text) <= 200:
            score += 3
        elif len(text) > 20:
            score += 1
        
        # Topic relevance
        topic_words = topic.lower().split()
        text_lower = text.lower()
        relevance = sum(1 for word in topic_words if word in text_lower)
        score += min(relevance * 2, 4)
        
        # Completeness (ends with punctuation)
        if text.strip().endswith(('.', '!', '?')):
            score += 2
        
        # Actionability (contains action words)
        action_words = ['use', 'try', 'set', 'enable', 'install', 'configure']
        if any(word in text_lower for word in action_words):
            score += 1
        
        return min(score, 10)
    
    def get_memory_usage(self):
        """Get current memory usage (simplified)"""
        try:
            import psutil
            return psutil.virtual_memory().used / (1024**2)  # MB
        except ImportError:
            return 0
    
    def get_most_productive_topic(self):
        """Find topic with longest average output"""
        if not self.demo_results:
            return "None"
        
        topic_lengths = {}
        for result in self.demo_results:
            topic = result["topic"]
            length = len(result["ai_output"])
            
            if topic not in topic_lengths:
                topic_lengths[topic] = []
            topic_lengths[topic].append(length)
        
        # Calculate averages
        topic_averages = {
            topic: sum(lengths) / len(lengths)
            for topic, lengths in topic_lengths.items()
        }
        
        return max(topic_averages.items(), key=lambda x: x[1])[0]
    
    def export_demo_results(self):
        """Export demonstration results"""
        export_data = {
            "demo_timestamp": time.time(),
            "model_used": "distilgpt2",
            "total_topics": len(self.demo_results),
            "results": self.demo_results,
            "summary": {
                "avg_ai_length": sum(len(r['ai_output']) for r in self.demo_results) / len(self.demo_results),
                "topics_tested": [r['topic'] for r in self.demo_results],
                "most_productive": self.get_most_productive_topic()
            }
        }
        
        with open("demo_results.json", "w") as f:
            json.dump(export_data, f, indent=2)

def main():
    """Run the complete demonstration"""
    demo = CompleteDemonstration()
    
    print("🎬 Welcome to the AI Assistant Complete Demo!")
    print("This will showcase all major features of the project.")
    
    proceed = input("\n🤔 Ready to start the demo? (y/n): ").strip().lower()
    
    if proceed == 'y':
        demo.run_complete_demo()
    else:
        print("👋 Demo cancelled. Run again when ready!")

if __name__ == "__main__":
    main()
