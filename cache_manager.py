#!/usr/bin/env python3
"""
Manage Hugging Face model cache
"""

import os
import shutil
from pathlib import Path

class HuggingFaceCacheManager:
    def __init__(self):
        self.cache_dir = Path.home() / ".cache" / "huggingface"
        
    def get_cache_info(self):
        """Get information about cached models"""
        if not self.cache_dir.exists():
            return {"total_size": 0, "models": [], "exists": False}
        
        total_size = 0
        models = []
        
        # Check transformers cache
        transformers_cache = self.cache_dir / "transformers"
        if transformers_cache.exists():
            for item in transformers_cache.iterdir():
                if item.is_dir():
                    size = self.get_dir_size(item)
                    total_size += size
                    models.append({
                        "name": item.name,
                        "size_mb": size / (1024**2),
                        "path": str(item)
                    })
        
        return {
            "total_size": total_size,
            "models": models,
            "exists": True,
            "cache_path": str(self.cache_dir)
        }
    
    def get_dir_size(self, path):
        """Calculate directory size"""
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    pass
        return total
    
    def display_cache_info(self):
        """Display cache information"""
        info = self.get_cache_info()
        
        if not info["exists"]:
            print("📁 No Hugging Face cache found")
            print("💡 Models will be downloaded on first use")
            return
        
        print(f"📁 Cache location: {info['cache_path']}")
        print(f"💾 Total cache size: {info['total_size'] / (1024**3):.2f} GB")
        
        if info["models"]:
            print(f"\n📦 Cached models ({len(info['models'])}):")
            for model in sorted(info["models"], key=lambda x: x["size_mb"], reverse=True):
                print(f"  • {model['name']}: {model['size_mb']:.1f} MB")
        else:
            print("\n📦 No models cached yet")
    
    def clear_cache(self):
        """Clear the entire cache"""
        if not self.cache_dir.exists():
            print("📁 No cache to clear")
            return
        
        try:
            shutil.rmtree(self.cache_dir)
            print("✅ Cache cleared successfully")
        except Exception as e:
            print(f"❌ Error clearing cache: {e}")
    
    def clear_specific_model(self, model_name):
        """Clear a specific model from cache"""
        transformers_cache = self.cache_dir / "transformers"
        
        if not transformers_cache.exists():
            print("📁 No transformers cache found")
            return
        
        # Find model directories that match the name
        cleared = False
        for item in transformers_cache.iterdir():
            if model_name.lower() in item.name.lower():
                try:
                    shutil.rmtree(item)
                    print(f"✅ Cleared {item.name}")
                    cleared = True
                except Exception as e:
                    print(f"❌ Error clearing {item.name}: {e}")
        
        if not cleared:
            print(f"❌ Model '{model_name}' not found in cache")

def main():
    manager = HuggingFaceCacheManager()
    
    print("🗂️  Hugging Face Cache Manager")
    print("=" * 40)
    
    while True:
        print("\n📋 Options:")
        print("1. Show cache info")
        print("2. Clear entire cache")
        print("3. Clear specific model")
        print("4. Check disk space")
        print("5. Quit")
        
        choice = input("\n> ").strip()
        
        if choice == "1":
            manager.display_cache_info()
            
        elif choice == "2":
            confirm = input("⚠️  Clear entire cache? This will delete all downloaded models (y/n): ")
            if confirm.lower() == 'y':
                manager.clear_cache()
            else:
                print("❌ Cancelled")
                
        elif choice == "3":
            model_name = input("Enter model name to clear: ").strip()
            if model_name:
                manager.clear_specific_model(model_name)
            else:
                print("❌ No model name provided")
                
        elif choice == "4":
            total, used, free = shutil.disk_usage("/")
            print(f"💾 Disk space:")
            print(f"  Total: {total / (1024**3):.1f} GB")
            print(f"  Used: {used / (1024**3):.1f} GB")
            print(f"  Free: {free / (1024**3):.1f} GB")
            
        elif choice == "5":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
