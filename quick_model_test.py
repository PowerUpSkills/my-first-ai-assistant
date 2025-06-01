#!/usr/bin/env python3
"""
Quick test of a better model (DistilGPT-2)
"""

from transformers import pipeline
import time

def test_distilgpt2():
    """Test DistilGPT-2 - smaller but often better than GPT-2"""
    
    print("🧪 Testing DistilGPT-2")
    print("📦 Size: ~350MB (smaller than GPT-2)")
    print("⚡ Speed: Faster than GPT-2")
    print("🎯 Quality: Often better than GPT-2")
    
    print("\n⏳ Loading DistilGPT-2 (first time will download)...")
    
    start_time = time.time()
    
    try:
        generator = pipeline(
            "text-generation",
            model="distilgpt2",
            max_length=100
        )
        
        load_time = time.time() - start_time
        print(f"✅ Loaded in {load_time:.1f} seconds")
        
        # Test the same prompt that gave poor results before
        prompt = "Mac productivity tip: Use"
        
        print(f"\n🎯 Testing prompt: '{prompt}'")
        print("📝 Generating 3 different responses...")
        
        for i in range(3):
            result = generator(
                prompt,
                max_length=80,
                temperature=0.7,
                do_sample=True,
                pad_token_id=50256
            )
            
            output = result[0]['generated_text']
            print(f"\n{i+1}. {output}")
        
        print(f"\n💡 Model cached at: ~/.cache/huggingface/")
        print(f"💡 Next time this will load instantly!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def compare_with_original():
    """Compare with your original GPT-2 results"""
    
    print("\n" + "="*60)
    print("📊 COMPARISON WITH YOUR ORIGINAL RESULTS")
    print("="*60)
    
    print("\n❌ Your Original GPT-2 Output:")
    print("• Start a spreadsheet with just one line of code...")
    print("• I'm starting to feel a bit tired. I want to watch Netflix...")
    print("• I've been running Windows 8...")
    
    print("\n✅ Expected DistilGPT-2 Improvement:")
    print("• More coherent sentences")
    print("• Better topic relevance") 
    print("• Fewer random tangents")
    print("• More Mac-related content")

if __name__ == "__main__":
    print("🚀 Quick Model Upgrade Test")
    print("=" * 40)
    
    success = test_distilgpt2()
    
    if success:
        compare_with_original()
        
        print("\n🎯 Next Steps:")
        print("1. Try 'gpt2-medium' for even better quality (~1.5GB)")
        print("2. Use model_comparison.py to test multiple models")
        print("3. Update your smart_writer.py to use the better model")
    else:
        print("\n❌ Test failed. Check your internet connection and try again.")
