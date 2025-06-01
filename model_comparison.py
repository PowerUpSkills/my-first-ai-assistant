#!/usr/bin/env python3
"""
Compare different models on the same productivity task
"""

from transformers import pipeline
import time

def test_productivity_generation():
    """Test different models for Mac productivity tips"""
    
    models = [
        "gpt2",                    # Your current model
        "distilgpt2",             # Faster, smaller version
        "gpt2-medium",            # Larger, potentially better
    ]
    
    prompt = "Mac productivity tip: Use"
    
    print("🧪 Comparing Models for Mac Productivity Tips")
    print("=" * 60)
    
    results = {}
    
    for model_name in models:
        print(f"\n🤖 Testing: {model_name}")
        print("-" * 40)
        
        try:
            # Load model
            print("⏳ Loading model...")
            start_time = time.time()
            
            generator = pipeline(
                "text-generation",
                model=model_name,
                max_length=100
            )
            
            load_time = time.time() - start_time
            print(f"✅ Loaded in {load_time:.1f}s")
            
            # Generate 3 different outputs
            outputs = []
            for i in range(3):
                result = generator(
                    prompt,
                    max_length=80,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=50256
                )
                outputs.append(result[0]['generated_text'])
            
            results[model_name] = {
                'load_time': load_time,
                'outputs': outputs
            }
            
            print("📝 Generated outputs:")
            for i, output in enumerate(outputs, 1):
                print(f"  {i}. {output}")
                
        except Exception as e:
            print(f"❌ Error with {model_name}: {str(e)}")
            results[model_name] = {'error': str(e)}
    
    # Summary comparison
    print("\n" + "="*60)
    print("📊 COMPARISON SUMMARY")
    print("="*60)
    
    for model_name, data in results.items():
        if 'error' in data:
            print(f"\n❌ {model_name}: Failed - {data['error']}")
        else:
            print(f"\n✅ {model_name}:")
            print(f"   ⏱️  Load time: {data['load_time']:.1f}s")
            print(f"   📝 Sample output: {data['outputs'][0][:100]}...")

def check_available_space():
    """Check available disk space"""
    import shutil
    
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024**3)
    
    print(f"💾 Available disk space: {free_gb:.1f} GB")
    
    if free_gb < 5:
        print("⚠️  Warning: Low disk space! Consider freeing up space before downloading large models.")
    else:
        print("✅ Sufficient space for model downloads")

if __name__ == "__main__":
    print("🚀 Model Download & Comparison Tool")
    print("=" * 50)
    
    check_available_space()
    
    print("\n💡 About Model Downloads:")
    print("• Models download to ~/.cache/huggingface/")
    print("• First download takes time, subsequent uses are fast")
    print("• You can delete cache anytime to free space")
    print("• Larger models generally produce better results")
    
    print("\n📦 Model Sizes:")
    print("• gpt2: ~500MB")
    print("• distilgpt2: ~350MB (faster)")
    print("• gpt2-medium: ~1.5GB (better quality)")
    
    proceed = input("\n🤔 Proceed with model testing? (y/n): ").strip().lower()
    
    if proceed == 'y':
        test_productivity_generation()
    else:
        print("👋 Cancelled. Run again when ready!")
