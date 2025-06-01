#!/usr/bin/env python3
"""
Simple demo to compare different models side by side
"""

from transformers import pipeline
import time

def test_model_quickly(model_name, prompt="Mac productivity tip: Use"):
    """Quick test of a model"""
    try:
        print(f"\n🧪 Testing {model_name}...")
        start = time.time()
        
        generator = pipeline("text-generation", model=model_name, max_length=80)
        load_time = time.time() - start
        
        result = generator(
            prompt,
            max_length=70,
            temperature=0.7,
            do_sample=True,
            pad_token_id=50256
        )
        
        output = result[0]['generated_text']
        print(f"⏱️  Load time: {load_time:.1f}s")
        print(f"📝 Output: {output}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 Quick Model Comparison Demo")
    print("=" * 50)
    
    print("\n💡 This will test different models with the same prompt")
    print("💡 First downloads may take time, subsequent uses are instant")
    
    models_to_try = [
        ("gpt2", "Your current model"),
        ("distilgpt2", "Recommended upgrade - smaller, often better"),
        ("gpt2-medium", "Much better quality (1.5GB download)")
    ]
    
    print(f"\n📋 Models to test:")
    for i, (model, desc) in enumerate(models_to_try, 1):
        print(f"{i}. {model} - {desc}")
    
    choice = input(f"\nWhich model to test? (1-{len(models_to_try)}) or 'all': ").strip()
    
    if choice.lower() == 'all':
        print("\n🔄 Testing all models...")
        for model, desc in models_to_try:
            test_model_quickly(model)
    elif choice.isdigit() and 1 <= int(choice) <= len(models_to_try):
        model, desc = models_to_try[int(choice) - 1]
        print(f"\n🔄 Testing {model}...")
        test_model_quickly(model)
    else:
        print("❌ Invalid choice")
        return
    
    print(f"\n✅ Demo complete!")
    print(f"💡 To use a model in your script, just change:")
    print(f"   pipeline('text-generation', model='MODEL_NAME')")

if __name__ == "__main__":
    main()
