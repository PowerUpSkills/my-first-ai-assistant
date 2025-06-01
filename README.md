# My First AI Assistant

A simple Python AI text generation application using Hugging Face Transformers and GPT-2.

## 🚀 Features

### 🎯 **Core AI Capabilities**
- **Text Generation** - GPT-2 powered creative writing and content creation
- **Document Summarization** - BART-Large-CNN for intelligent text summarization
- **Sentiment Analysis** - Emotion detection and opinion analysis
- **Question Answering** - Extract answers from provided context

### 🛠️ **Technical Features**
- GPU acceleration support (MPS on Apple Silicon, CUDA on NVIDIA)
- Automatic model downloading and caching
- Multiple applications for different use cases
- Clean, production-ready code structure

### 💼 **Business Applications**
- Content marketing automation
- Customer support enhancement
- Research and document analysis
- Educational content creation

## 📋 Prerequisites

- Python 3.8 or higher
- macOS, Linux, or Windows
- Internet connection (for initial model download)

## 🛠️ Installation

### Step 1: Install uv (Python Package Manager)

`uv` is a fast Python package installer and resolver. Install it using one of these methods:

#### On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Alternative (using pip):
```bash
pip install uv
```

### Step 2: Clone or Download the Project

```bash
git clone <your-repo-url>
cd my-first-ai-asssistant
```

Or download the files manually and navigate to the project directory.

### Step 3: Create Virtual Environment with uv

```bash
uv venv
```

This creates a `.venv` directory with an isolated Python environment.

### Step 4: Install Dependencies

```bash
uv pip install -r requirements.txt
```

This will install:
- `transformers>=4.30.0` - Hugging Face Transformers library
- `torch>=2.0.0` - PyTorch for deep learning
- `numpy` - Numerical computing library

## 🎯 Usage

### Activate the Virtual Environment

Before running the application, activate the virtual environment:

#### On macOS/Linux:
```bash
source .venv/bin/activate
```

#### On Windows:
```bash
.venv\Scripts\activate
```

### Run the Applications

Choose the application that fits your needs:

#### 🎓 **Learning AI Basics**
```bash
python my_first_ai.py
```
Simple text generation to understand AI fundamentals.

#### ✍️ **Content Creation & Writing**
```bash
python smart_writer.py
```
Interactive writing assistant with brainstorming capabilities.

#### 🚀 **Business Automation (Recommended)**
```bash
python ai_toolkit.py
```
Complete AI platform with 4 tools: text generation, summarization, sentiment analysis, and Q&A.

### First Run

On the first run, the application will:
1. Download the GPT-2 model (~548MB) from Hugging Face
2. Cache the model locally for future use
3. Generate text based on the prompt: "The best thing about being a developer is"

### Expected Output

```
The best thing about being a developer is [generated text continues...]
```

## 🔧 Customization

### Modify the Prompt

Edit the `my_first_ai` file and change the prompt:

```python
prompt = "Your custom prompt here"
```

### Adjust Generation Parameters

You can modify the text generation parameters:

```python
result = generator(
    prompt, 
    max_length=100,        # Maximum total length
    max_new_tokens=50,     # Maximum new tokens to generate
    temperature=0.7,       # Creativity (0.1-1.0)
    do_sample=True,        # Enable sampling
    pad_token_id=50256     # Padding token
)
```

## 📁 Project Structure

```
my-first-ai-assistant/
├── 📄 Core Applications
│   ├── my_first_ai.py              # Simple AI text generator (learning)
│   ├── smart_writer.py             # Enhanced writing assistant (content creation)
│   ├── ai_toolkit.py               # Multi-purpose AI platform (business automation)
│   └── requirements.txt            # Python dependencies
│
├── 🛠️ Utilities
│   ├── cache_manager.py            # Model cache management
│   └── demo_complete_features.py   # Feature demonstration
│
├── 📚 Documentation
│   ├── README.md                   # This file
│   └── CURRENT_PROJECT_STRUCTURE.md # Detailed project overview
│
└── 🔧 Environment
    └── .venv/                      # Virtual environment (created after setup)
```

## 🐛 Troubleshooting

### Common Issues

1. **Model Download Fails**
   - Check internet connection
   - Ensure sufficient disk space (~1GB)
   - Try running again (downloads resume automatically)

2. **GPU Not Detected**
   - On Apple Silicon: Ensure macOS 12.3+ for MPS support
   - On NVIDIA: Install CUDA-compatible PyTorch version
   - CPU fallback works automatically

3. **Memory Issues**
   - Reduce `max_length` parameter
   - Close other applications
   - Ensure at least 4GB RAM available

### Performance Tips

- **First run**: Model download may take 5-10 minutes
- **Subsequent runs**: Model loads from cache (~10-30 seconds)
- **GPU acceleration**: Significantly faster on compatible hardware

## 🔄 Managing Dependencies with uv

### Add New Packages
```bash
uv pip install package-name
```

### Update Requirements File
```bash
uv pip freeze > requirements.txt
```

### Install from Updated Requirements
```bash
uv pip install -r requirements.txt
```

### Remove Packages
```bash
uv pip uninstall package-name
```

## 🧹 Cleanup

### Deactivate Virtual Environment
```bash
deactivate
```

### Remove Virtual Environment
```bash
rm -rf .venv
```

## 📚 Learn More

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [uv Documentation](https://docs.astral.sh/uv/)

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
