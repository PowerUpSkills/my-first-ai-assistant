# smart_writer.py
from transformers import pipeline
import os
import re

class MyWritingAssistant:
    def __init__(self, model_name="gpt2"):
        print("🤖 Starting up your AI writing buddy...")
        print(f"📦 Loading model: {model_name}")

        # Try to use a better model if available
        try:
            self.generator = pipeline(
                "text-generation",
                model=model_name,
                max_length=150,
                device=0 if model_name != "gpt2" else -1  # Use GPU for larger models
            )
        except Exception as e:
            print(f"⚠️  Could not load {model_name}, falling back to GPT-2")
            self.generator = pipeline(
                "text-generation",
                model="gpt2",
                max_length=150
            )
        print("✅ Ready to help with your writing!")

    def clean_output(self, text, max_sentences=3):
        """Clean and limit the generated text"""
        # Split into sentences and take only the first few
        sentences = re.split(r'[.!?]+', text)
        # Filter out very short or incomplete sentences
        good_sentences = [s.strip() for s in sentences[:max_sentences] if len(s.strip()) > 10]
        return '. '.join(good_sentences) + '.' if good_sentences else text[:100] + '...'

    def complete_sentence(self, text):
        """Help finish thoughts with improved parameters"""
        result = self.generator(
            text,
            max_length=len(text.split()) + 40,
            num_return_sequences=2,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.1,
            truncation=True,
            pad_token_id=50256
        )
        return [r['generated_text'] for r in result]
    
    def brainstorm_ideas(self, topic):
        """Generate creative ideas with better prompts and parameters"""
        # More specific and structured prompts
        prompts = [
            f"Here are 3 effective {topic} techniques:\n1.",
            f"Quick {topic} tips:\n- ",
            f"Best practices for {topic}:\nFirst,"
        ]

        ideas = []
        for i, prompt in enumerate(prompts):
            try:
                result = self.generator(
                    prompt,
                    max_length=100,
                    temperature=0.7,  # Lower temperature for more focused output
                    do_sample=True,
                    top_p=0.8,
                    repetition_penalty=1.2,
                    truncation=True,
                    pad_token_id=50256
                )

                generated_text = result[0]['generated_text']
                # Clean and format the output
                clean_text = self.clean_output(generated_text, max_sentences=2)
                ideas.append(clean_text)

            except Exception as e:
                ideas.append(f"Error generating idea {i+1}: {str(e)}")

        return ideas
def main():
    assistant = MyWritingAssistant()
    
    print("\n🚀 What can I help you write today?")
    print("Commands: 'complete', 'brainstorm', 'quit'")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == 'quit':
            print("Happy writing! 👋")
            break
            
        elif command == 'complete':
            text = input("Start your sentence: ")
            options = assistant.complete_sentence(text)
            print("\n💡 Here are two ways to continue:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
                
        elif command == 'brainstorm':
            topic = input("What topic? ")
            ideas = assistant.brainstorm_ideas(topic)
            print(f"\n🎯 Ideas about '{topic}':")
            for idea in ideas:
                print(f"• {idea}")
                
        else:
            print("Try 'complete', 'brainstorm', or 'quit'")
if __name__ == "__main__":
    main()