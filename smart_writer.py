# smart_writer_improved.py
from transformers import pipeline
import re

class ImprovedWritingAssistant:
    def __init__(self, model_name="distilgpt2"):
        print("🤖 Starting up your improved AI writing buddy...")
        print(f"📦 Using model: {model_name}")

        # Model options with descriptions
        model_info = {
            "gpt2": "Original GPT-2 (500MB, basic quality)",
            "distilgpt2": "DistilGPT-2 (350MB, faster, often better)",
            "gpt2-medium": "GPT-2 Medium (1.5GB, better quality)",
            "gpt2-large": "GPT-2 Large (3GB, best quality)"
        }

        if model_name in model_info:
            print(f"ℹ️  {model_info[model_name]}")

        try:
            self.generator = pipeline(
                "text-generation",
                model=model_name,
                max_length=120
            )
            print("✅ Ready to help with better writing!")
        except Exception as e:
            print(f"⚠️  Could not load {model_name}, falling back to GPT-2")
            self.generator = pipeline(
                "text-generation",
                model="gpt2",
                max_length=120
            )
            print("✅ Ready to help with basic writing!")
    
    def clean_output(self, text, max_length=200):
        """Clean and limit the generated text"""
        # Remove extra whitespace and newlines
        text = ' '.join(text.split())
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        
        # Take first few complete sentences
        result = ""
        for sentence in sentences[:3]:
            sentence = sentence.strip()
            if len(sentence) > 10 and len(result + sentence) < max_length:
                result += sentence + ". "
        
        return result.strip() if result else text[:max_length] + "..."
    
    def brainstorm_ideas(self, topic):
        """Generate ideas with improved prompts and cleaning"""
        
        # Better structured prompts
        prompts = [
            f"Mac productivity tip: Use",
            f"To improve {topic}, try",
            f"Quick {topic} hack:"
        ]
        
        ideas = []
        for prompt in prompts:
            try:
                result = self.generator(
                    prompt,
                    max_length=80,
                    temperature=0.6,  # Lower temperature for more focused output
                    do_sample=True,
                    pad_token_id=50256
                )
                
                generated_text = result[0]['generated_text']
                clean_text = self.clean_output(generated_text)
                ideas.append(clean_text)
                
            except Exception as e:
                ideas.append(f"Could not generate idea: {str(e)}")
        
        return ideas
    
    def get_curated_tips(self, topic):
        """Provide curated tips as fallback"""
        mac_tips = {
            "productivity hacks on a mac": [
                "Use Spotlight Search (Cmd+Space) to quickly find anything on your Mac",
                "Set up Hot Corners in System Preferences for instant access to features",
                "Use Mission Control (F3) to organize multiple desktops and windows",
                "Master keyboard shortcuts: Cmd+Tab (app switcher), Cmd+` (window switcher)",
                "Install Alfred or Raycast for advanced automation and quick actions"
            ],
            "mac workflow": [
                "Use the Shortcuts app to automate repetitive tasks",
                "Set up text replacements in System Preferences for common phrases",
                "Use Focus modes to minimize distractions during work",
                "Organize files with smart folders and tags",
                "Use Handoff to seamlessly switch between Mac and iPhone/iPad"
            ]
        }
        
        # Find matching tips
        for key, tips in mac_tips.items():
            if any(word in topic.lower() for word in key.split()):
                return tips[:3]  # Return first 3 tips
        
        return ["No specific tips available for this topic"]

def main():
    print("🤖 AI Writing Assistant")
    print("=" * 30)

    # Let user choose model
    print("\n📦 Available models:")
    print("1. distilgpt2 (Default - 350MB, fast, good quality)")
    print("2. gpt2 (Original - 500MB, basic quality)")
    print("3. gpt2-medium (1.5GB, better quality)")
    print("4. gpt2-large (3GB, best quality)")

    choice = input("\nChoose model (1-4) or press Enter for default: ").strip()

    model_map = {
        "1": "distilgpt2",
        "2": "gpt2",
        "3": "gpt2-medium",
        "4": "gpt2-large",
        "": "distilgpt2"  # default
    }

    model_name = model_map.get(choice, "distilgpt2")

    assistant = ImprovedWritingAssistant(model_name)

    print("\n🚀 What can I help you write today?")
    print("Commands: 'brainstorm', 'curated', 'quit'")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == 'quit':
            print("Happy writing! 👋")
            break
            
        elif command == 'brainstorm':
            topic = input("What topic? ")
            print(f"\n🎯 AI-generated ideas about '{topic}':")
            ideas = assistant.brainstorm_ideas(topic)
            for i, idea in enumerate(ideas, 1):
                print(f"{i}. {idea}")
                
        elif command == 'curated':
            topic = input("What topic? ")
            print(f"\n📚 Curated tips for '{topic}':")
            tips = assistant.get_curated_tips(topic)
            for i, tip in enumerate(tips, 1):
                print(f"{i}. {tip}")
                
        else:
            print("Try 'brainstorm', 'curated', or 'quit'")

if __name__ == "__main__":
    main()
