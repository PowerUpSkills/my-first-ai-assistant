#!/usr/bin/env python3
"""
Test different Hugging Face models for text generation
"""

from transformers import pipeline
import time

class ModelTester:
    def __init__(self):
        self.models_to_test = [
            {
                "name": "gpt2",
                "description": "Original GPT-2 (117M params, ~500MB)",
                "size": "Small"
            },
            {
                "name": "gpt2-medium", 
                "description": "GPT-2 Medium (345M params, ~1.5GB)",
                "size": "Medium"
            },
            {
                "name": "distilgpt2",
                "description": "DistilGPT-2 (82M params, ~350MB) - Faster",
                "size": "Small"
            },
            {
                "name": "microsoft/DialoGPT-small",
                "description": "DialoGPT Small (117M params, ~500MB) - Conversational",
                "size": "Small"
            }
        ]
    
    def test_model(self, model_info, prompt="Mac productivity tip: Use"):
        """Test a single model"""
        print(f"\n🧪 Testing: {model_info['name']}")
        print(f"📝 Description: {model_info['description']}")
        print(f"📦 Size: {model_info['size']}")
        
        try:
            print("⏳ Loading model (this may take a while for first download)...")
            start_time = time.time()
            
            generator = pipeline(
                "text-generation",
                model=model_info['name'],
                max_length=100
            )
            
            load_time = time.time() - start_time
            print(f"✅ Loaded in {load_time:.1f} seconds")
            
            # Generate text
            print("🎯 Generating text...")
            result = generator(
                prompt,
                max_length=80,
                temperature=0.7,
                do_sample=True,
                pad_token_id=50256
            )
            
            print(f"📄 Output: {result[0]['generated_text']}")
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def check_cache_size(self):
        """Check current Hugging Face cache size"""
        import os
        cache_dir = os.path.expanduser("~/.cache/huggingface/")
        
        if os.path.exists(cache_dir):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(cache_dir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(filepath)
            
            size_gb = total_size / (1024**3)
            print(f"💾 Current cache size: {size_gb:.2f} GB")
            print(f"📁 Cache location: {cache_dir}")
        else:
            print("📁 No Hugging Face cache found yet")
    
    def interactive_test(self):
        """Interactive model testing"""
        print("🤖 Hugging Face Model Tester")
        print("=" * 50)
        
        self.check_cache_size()
        
        print("\n📋 Available models to test:")
        for i, model in enumerate(self.models_to_test, 1):
            print(f"{i}. {model['name']} - {model['description']}")
        
        print("\n💡 Note: First download of each model will take time!")
        print("💡 Subsequent uses will be much faster (loaded from cache)")
        
        while True:
            print("\n" + "="*50)
            choice = input("\nEnter model number to test (1-4), 'all' for all models, or 'quit': ").strip()
            
            if choice.lower() == 'quit':
                break
            elif choice.lower() == 'all':
                for model in self.models_to_test:
                    self.test_model(model)
            elif choice.isdigit() and 1 <= int(choice) <= len(self.models_to_test):
                model = self.models_to_test[int(choice) - 1]
                self.test_model(model)
            else:
                print("❌ Invalid choice. Please try again.")
        
        print("\n👋 Testing complete!")
        self.check_cache_size()

def main():
    tester = ModelTester()
    tester.interactive_test()

if __name__ == "__main__":
    main()
