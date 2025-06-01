# 🚀 Advanced AI Assistant Guide

## 📚 Table of Contents
1. [Model Selection & Performance](#model-selection--performance)
2. [Advanced Configuration](#advanced-configuration)
3. [Prompt Engineering Best Practices](#prompt-engineering-best-practices)
4. [Performance Optimization](#performance-optimization)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)
6. [Extending Functionality](#extending-functionality)

## 🤖 Model Selection & Performance

### Available Models Comparison

| Model | Size | Parameters | Quality | Speed | Memory Usage | Best For |
|-------|------|------------|---------|-------|--------------|----------|
| `gpt2` | 500MB | 117M | ⭐⭐ | ⚡⚡⚡ | Low | Learning/Testing |
| `distilgpt2` | 350MB | 82M | ⭐⭐⭐ | ⚡⚡⚡⚡ | Low | **Recommended Start** |
| `gpt2-medium` | 1.5GB | 345M | ⭐⭐⭐⭐ | ⚡⚡ | Medium | Quality Content |
| `gpt2-large` | 3GB | 774M | ⭐⭐⭐⭐⭐ | ⚡ | High | Maximum Quality |

### Performance Benchmarks

```python
# Typical load times (after download)
gpt2:        2-5 seconds
distilgpt2:  1-3 seconds  
gpt2-medium: 5-10 seconds
gpt2-large:  10-20 seconds

# Generation speed (tokens/second)
gpt2:        ~50 tokens/sec
distilgpt2:  ~70 tokens/sec
gpt2-medium: ~30 tokens/sec
gpt2-large:  ~15 tokens/sec
```

## ⚙️ Advanced Configuration

### Custom Model Configuration

```python
# smart_writer_advanced.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class AdvancedWritingAssistant:
    def __init__(self, model_name="distilgpt2", device="auto"):
        self.model_name = model_name
        self.device = self._get_device(device)
        
        # Load with custom configuration
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device != "cpu" else torch.float32,
            device_map=self.device
        )
        
        # Set pad token if not exists
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
    
    def _get_device(self, device):
        """Automatically detect best device"""
        if device == "auto":
            if torch.cuda.is_available():
                return "cuda"
            elif torch.backends.mps.is_available():
                return "mps"
            else:
                return "cpu"
        return device
    
    def generate_with_custom_params(self, prompt, **kwargs):
        """Generate with fine-tuned parameters"""
        default_params = {
            "max_length": 100,
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "repetition_penalty": 1.1,
            "do_sample": True,
            "pad_token_id": self.tokenizer.eos_token_id
        }
        
        # Override defaults with user params
        params = {**default_params, **kwargs}
        
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(inputs, **params)
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Environment-Specific Optimizations

```python
# config.py
import torch
import platform

class Config:
    def __init__(self):
        self.system = platform.system()
        self.device = self._detect_device()
        self.model_settings = self._get_model_settings()
    
    def _detect_device(self):
        """Detect optimal device configuration"""
        if torch.cuda.is_available():
            return {
                "device": "cuda",
                "dtype": torch.float16,
                "memory_efficient": True
            }
        elif torch.backends.mps.is_available() and self.system == "Darwin":
            return {
                "device": "mps", 
                "dtype": torch.float32,  # MPS doesn't support float16 well
                "memory_efficient": False
            }
        else:
            return {
                "device": "cpu",
                "dtype": torch.float32,
                "memory_efficient": False
            }
    
    def _get_model_settings(self):
        """Get recommended model based on system"""
        if self.device["device"] == "cuda":
            return {
                "recommended": "gpt2-large",
                "fallback": "gpt2-medium",
                "batch_size": 4
            }
        elif self.device["device"] == "mps":
            return {
                "recommended": "gpt2-medium", 
                "fallback": "distilgpt2",
                "batch_size": 2
            }
        else:
            return {
                "recommended": "distilgpt2",
                "fallback": "gpt2",
                "batch_size": 1
            }
```

## 🎯 Prompt Engineering Best Practices

### Effective Prompt Templates

```python
# prompt_templates.py
class PromptTemplates:
    
    @staticmethod
    def productivity_tips(topic, num_tips=3):
        return f"""
You are a productivity expert. Provide {num_tips} specific, actionable tips for {topic}.

Format each tip as:
• [Action]: [Specific instruction] - [Expected benefit]

Tips for {topic}:
"""
    
    @staticmethod
    def structured_advice(topic, format_type="numbered"):
        formats = {
            "numbered": "1. [Tip]\n2. [Tip]\n3. [Tip]",
            "bullet": "• [Tip]\n• [Tip]\n• [Tip]",
            "steps": "Step 1: [Action]\nStep 2: [Action]\nStep 3: [Action]"
        }
        
        return f"""
Provide practical advice for {topic} in this exact format:

{formats[format_type]}

Advice for {topic}:
"""
    
    @staticmethod
    def creative_brainstorm(topic, perspective="expert"):
        perspectives = {
            "expert": "You are an expert consultant",
            "beginner": "You are helping a complete beginner", 
            "creative": "You are a creative problem solver",
            "technical": "You are a technical specialist"
        }
        
        return f"""
{perspectives[perspective]} providing ideas about {topic}.

Generate 3 unique approaches:
1. Traditional approach: [Description]
2. Innovative approach: [Description] 
3. Unconventional approach: [Description]

Ideas for {topic}:
"""

# Usage example
def generate_better_content(assistant, topic):
    templates = PromptTemplates()
    
    # Try different prompt styles
    prompts = [
        templates.productivity_tips(topic),
        templates.structured_advice(topic, "bullet"),
        templates.creative_brainstorm(topic, "expert")
    ]
    
    results = []
    for prompt in prompts:
        result = assistant.generate(prompt)
        results.append(result)
    
    return results
```

### Quality Filtering

```python
# quality_filter.py
import re

class OutputQualityFilter:
    
    @staticmethod
    def is_relevant(text, topic_keywords):
        """Check if output is relevant to topic"""
        text_lower = text.lower()
        topic_words = [word.lower() for word in topic_keywords]
        
        relevance_score = sum(1 for word in topic_words if word in text_lower)
        return relevance_score >= len(topic_words) * 0.3  # 30% keyword match
    
    @staticmethod
    def is_complete(text, min_length=50):
        """Check if output is complete and coherent"""
        # Remove extra whitespace
        clean_text = ' '.join(text.split())
        
        # Check minimum length
        if len(clean_text) < min_length:
            return False
        
        # Check for incomplete sentences
        if text.endswith(('...', '..', '.')):
            return True
        
        # Check if ends abruptly
        last_char = text.strip()[-1] if text.strip() else ''
        return last_char in '.!?'
    
    @staticmethod
    def remove_artifacts(text):
        """Clean common AI generation artifacts"""
        # Remove HTML-like tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove repeated punctuation
        text = re.sub(r'[.]{3,}', '...', text)
        text = re.sub(r'[!]{2,}', '!', text)
        text = re.sub(r'[?]{2,}', '?', text)
        
        # Remove incomplete URLs
        text = re.sub(r'https?://[^\s]*(?=\s|$)', '[URL]', text)
        
        return text.strip()
    
    @classmethod
    def filter_output(cls, text, topic_keywords, min_quality_score=0.7):
        """Comprehensive output filtering"""
        # Clean artifacts
        clean_text = cls.remove_artifacts(text)
        
        # Check relevance
        is_relevant = cls.is_relevant(clean_text, topic_keywords)
        
        # Check completeness
        is_complete = cls.is_complete(clean_text)
        
        # Calculate quality score
        quality_score = 0
        if is_relevant:
            quality_score += 0.5
        if is_complete:
            quality_score += 0.3
        if len(clean_text.split()) >= 10:  # Reasonable length
            quality_score += 0.2
        
        return {
            "text": clean_text,
            "quality_score": quality_score,
            "is_acceptable": quality_score >= min_quality_score,
            "issues": {
                "relevance": not is_relevant,
                "completeness": not is_complete,
                "length": len(clean_text.split()) < 10
            }
        }
```

## 🔧 Performance Optimization

### Memory Management

```python
# memory_optimizer.py
import torch
import gc
from contextlib import contextmanager

class MemoryOptimizer:
    
    @staticmethod
    @contextmanager
    def memory_efficient_generation():
        """Context manager for memory-efficient generation"""
        try:
            # Clear cache before generation
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            elif torch.backends.mps.is_available():
                torch.mps.empty_cache()
            
            yield
            
        finally:
            # Clean up after generation
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            elif torch.backends.mps.is_available():
                torch.mps.empty_cache()
    
    @staticmethod
    def optimize_model_loading(model_name, device="auto"):
        """Load model with memory optimizations"""
        load_config = {
            "torch_dtype": torch.float16 if device != "cpu" else torch.float32,
            "low_cpu_mem_usage": True,
            "device_map": device if device != "auto" else None
        }
        
        # Additional optimizations for large models
        if "large" in model_name:
            load_config.update({
                "load_in_8bit": True,  # Requires bitsandbytes
                "device_map": "auto"
            })
        
        return load_config

# Usage in your assistant
class OptimizedWritingAssistant:
    def __init__(self, model_name="distilgpt2"):
        self.optimizer = MemoryOptimizer()
        
        with self.optimizer.memory_efficient_generation():
            self.generator = pipeline(
                "text-generation",
                model=model_name,
                **self.optimizer.optimize_model_loading(model_name)
            )
    
    def generate(self, prompt, **kwargs):
        with self.optimizer.memory_efficient_generation():
            return self.generator(prompt, **kwargs)
```

### Batch Processing

```python
# batch_processor.py
class BatchProcessor:
    
    def __init__(self, assistant, batch_size=3):
        self.assistant = assistant
        self.batch_size = batch_size
    
    def generate_multiple_ideas(self, topics, prompts_per_topic=3):
        """Generate ideas for multiple topics efficiently"""
        all_prompts = []
        topic_mapping = []
        
        # Prepare all prompts
        for topic in topics:
            for i in range(prompts_per_topic):
                prompt = f"Productivity tip for {topic}: "
                all_prompts.append(prompt)
                topic_mapping.append(topic)
        
        # Process in batches
        results = {}
        for i in range(0, len(all_prompts), self.batch_size):
            batch = all_prompts[i:i + self.batch_size]
            batch_topics = topic_mapping[i:i + self.batch_size]
            
            # Generate batch
            batch_results = []
            for prompt in batch:
                result = self.assistant.generate(prompt)
                batch_results.append(result)
            
            # Organize results by topic
            for topic, result in zip(batch_topics, batch_results):
                if topic not in results:
                    results[topic] = []
                results[topic].append(result)
        
        return results
```

## 🔧 Troubleshooting Common Issues

### Model Loading Issues

```python
# troubleshooter.py
import torch
import psutil
import os

class TroubleshootingGuide:

    @staticmethod
    def diagnose_system():
        """Diagnose system capabilities"""
        print("🔍 System Diagnosis")
        print("=" * 30)

        # Memory check
        memory = psutil.virtual_memory()
        print(f"💾 RAM: {memory.total / (1024**3):.1f} GB total, {memory.available / (1024**3):.1f} GB available")

        # GPU check
        if torch.cuda.is_available():
            print(f"🎮 CUDA GPU: {torch.cuda.get_device_name()}")
            print(f"   VRAM: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.1f} GB")
        elif torch.backends.mps.is_available():
            print("🍎 Apple Silicon GPU: Available")
        else:
            print("💻 CPU only (no GPU acceleration)")

        # Disk space check
        disk = psutil.disk_usage('/')
        print(f"💿 Disk: {disk.free / (1024**3):.1f} GB free")

        # Recommendations
        print("\n💡 Recommendations:")
        if memory.available < 4 * (1024**3):  # Less than 4GB
            print("⚠️  Low memory - use distilgpt2 or gpt2")
        if disk.free < 5 * (1024**3):  # Less than 5GB
            print("⚠️  Low disk space - avoid large models")

    @staticmethod
    def fix_common_errors():
        """Common error fixes"""
        fixes = {
            "CUDA out of memory": [
                "Use smaller model (distilgpt2 instead of gpt2-large)",
                "Reduce max_length parameter",
                "Clear CUDA cache: torch.cuda.empty_cache()",
                "Restart Python session"
            ],
            "Model download fails": [
                "Check internet connection",
                "Clear cache: rm -rf ~/.cache/huggingface/",
                "Try different model mirror",
                "Use VPN if in restricted region"
            ],
            "Slow generation": [
                "Use GPU if available",
                "Reduce max_length",
                "Use distilgpt2 for speed",
                "Close other applications"
            ],
            "Poor output quality": [
                "Use larger model (gpt2-medium)",
                "Improve prompts with examples",
                "Adjust temperature (0.6-0.8)",
                "Use output filtering"
            ]
        }

        print("🛠️  Common Issues & Fixes")
        print("=" * 30)
        for issue, solutions in fixes.items():
            print(f"\n❌ {issue}:")
            for solution in solutions:
                print(f"   ✅ {solution}")

# Quick diagnostic script
def run_diagnostics():
    troubleshooter = TroubleshootingGuide()
    troubleshooter.diagnose_system()
    print("\n")
    troubleshooter.fix_common_errors()
```

### Performance Monitoring

```python
# performance_monitor.py
import time
import psutil
import torch
from contextlib import contextmanager

class PerformanceMonitor:

    @contextmanager
    def monitor_generation(self, operation_name="Generation"):
        """Monitor performance during text generation"""
        # Start monitoring
        start_time = time.time()
        start_memory = psutil.virtual_memory().used

        if torch.cuda.is_available():
            start_gpu_memory = torch.cuda.memory_allocated()
        else:
            start_gpu_memory = 0

        try:
            yield
        finally:
            # End monitoring
            end_time = time.time()
            end_memory = psutil.virtual_memory().used

            if torch.cuda.is_available():
                end_gpu_memory = torch.cuda.memory_allocated()
            else:
                end_gpu_memory = 0

            # Report results
            duration = end_time - start_time
            memory_delta = (end_memory - start_memory) / (1024**2)  # MB
            gpu_memory_delta = (end_gpu_memory - start_gpu_memory) / (1024**2)  # MB

            print(f"\n📊 {operation_name} Performance:")
            print(f"   ⏱️  Duration: {duration:.2f} seconds")
            print(f"   💾 RAM used: {memory_delta:+.1f} MB")
            if gpu_memory_delta != 0:
                print(f"   🎮 GPU RAM used: {gpu_memory_delta:+.1f} MB")

# Usage example
monitor = PerformanceMonitor()

with monitor.monitor_generation("Model Loading"):
    assistant = MyWritingAssistant()

with monitor.monitor_generation("Text Generation"):
    result = assistant.brainstorm_ideas("productivity hacks")
```

## 🚀 Extending Functionality

### Custom Features

```python
# extensions.py
import json
import datetime
from pathlib import Path

class AdvancedFeatures:

    def __init__(self, assistant):
        self.assistant = assistant
        self.history_file = Path("generation_history.json")
        self.favorites_file = Path("favorite_outputs.json")

    def save_generation_history(self, prompt, output, model_used):
        """Save generation history for analysis"""
        history_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "prompt": prompt,
            "output": output,
            "model": model_used,
            "quality_score": self._calculate_quality_score(output)
        }

        # Load existing history
        history = self._load_json(self.history_file, [])
        history.append(history_entry)

        # Keep only last 100 entries
        history = history[-100:]

        # Save updated history
        self._save_json(self.history_file, history)

    def save_favorite(self, output, tags=None):
        """Save favorite outputs"""
        favorite = {
            "timestamp": datetime.datetime.now().isoformat(),
            "output": output,
            "tags": tags or [],
            "id": len(self._load_json(self.favorites_file, []))
        }

        favorites = self._load_json(self.favorites_file, [])
        favorites.append(favorite)
        self._save_json(self.favorites_file, favorites)

        print(f"✅ Saved to favorites (ID: {favorite['id']})")

    def search_history(self, keyword):
        """Search generation history"""
        history = self._load_json(self.history_file, [])
        matches = []

        for entry in history:
            if keyword.lower() in entry['prompt'].lower() or keyword.lower() in entry['output'].lower():
                matches.append(entry)

        return matches

    def get_analytics(self):
        """Get usage analytics"""
        history = self._load_json(self.history_file, [])

        if not history:
            return "No history available"

        # Calculate stats
        total_generations = len(history)
        avg_quality = sum(entry.get('quality_score', 0) for entry in history) / total_generations
        models_used = {}

        for entry in history:
            model = entry.get('model', 'unknown')
            models_used[model] = models_used.get(model, 0) + 1

        most_used_model = max(models_used.items(), key=lambda x: x[1])

        return {
            "total_generations": total_generations,
            "average_quality": avg_quality,
            "most_used_model": most_used_model[0],
            "models_usage": models_used
        }

    def _calculate_quality_score(self, text):
        """Simple quality scoring"""
        score = 0

        # Length check
        if 50 <= len(text) <= 200:
            score += 0.3

        # Sentence structure
        sentences = text.split('.')
        if 2 <= len(sentences) <= 5:
            score += 0.3

        # No repetition
        words = text.lower().split()
        unique_ratio = len(set(words)) / len(words) if words else 0
        if unique_ratio > 0.7:
            score += 0.4

        return min(score, 1.0)

    def _load_json(self, file_path, default):
        """Load JSON file safely"""
        try:
            if file_path.exists():
                with open(file_path, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return default

    def _save_json(self, file_path, data):
        """Save JSON file safely"""
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving {file_path}: {e}")

# Interactive features
class InteractiveFeatures:

    def __init__(self, assistant):
        self.assistant = assistant
        self.advanced = AdvancedFeatures(assistant)

    def interactive_improvement(self, prompt):
        """Iteratively improve output"""
        print(f"🎯 Improving output for: '{prompt}'")

        attempts = []
        for i in range(3):
            print(f"\n🔄 Attempt {i+1}:")

            # Generate with different parameters
            temp = 0.5 + (i * 0.2)  # Vary temperature
            result = self.assistant.generate(
                prompt,
                temperature=temp,
                max_length=80
            )

            attempts.append({
                "attempt": i+1,
                "temperature": temp,
                "output": result,
                "quality": self.advanced._calculate_quality_score(result)
            })

            print(f"📝 Output: {result}")
            print(f"📊 Quality: {attempts[-1]['quality']:.2f}")

        # Find best attempt
        best = max(attempts, key=lambda x: x['quality'])
        print(f"\n🏆 Best result (Attempt {best['attempt']}):")
        print(f"📝 {best['output']}")

        return best['output']

    def collaborative_editing(self, initial_output):
        """Allow user to collaboratively edit output"""
        print(f"✏️  Collaborative Editing")
        print(f"Original: {initial_output}")

        while True:
            action = input("\nActions: (e)dit, (r)egenerate, (s)ave, (q)uit: ").lower()

            if action == 'e':
                # Manual editing
                edited = input("Enter your edited version: ")
                print(f"✅ Updated: {edited}")
                initial_output = edited

            elif action == 'r':
                # Regenerate with feedback
                feedback = input("What should be improved? ")
                new_prompt = f"Improve this text based on feedback '{feedback}': {initial_output}"
                regenerated = self.assistant.generate(new_prompt)
                print(f"🔄 Regenerated: {regenerated}")
                initial_output = regenerated

            elif action == 's':
                # Save to favorites
                tags = input("Add tags (comma-separated): ").split(',')
                tags = [tag.strip() for tag in tags if tag.strip()]
                self.advanced.save_favorite(initial_output, tags)

            elif action == 'q':
                break

        return initial_output
```

This completes the advanced guide with troubleshooting, performance monitoring, and extended functionality. The guide now covers everything from basic usage to advanced features like history tracking, analytics, and collaborative editing.
