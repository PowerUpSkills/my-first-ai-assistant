# ai_toolkit.py
from transformers import pipeline

class AIToolkit:
    def __init__(self):
        print("🔧 Loading AI toolkit...")
        
        # Different specialized models
        self.text_generator = pipeline("text-generation", model="gpt2")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.qa_system = pipeline("question-answering")
        
        print("✅ All tools ready!")
    
    def write_with_me(self, prompt):
        """Creative writing assistant"""
        result = self.text_generator(
            prompt, 
            max_length=100, 
            temperature=0.8,
            do_sample=True
        )
        return result[0]['generated_text']
    
    def tldr_this(self, long_text):
        """Summarize long content"""
        if len(long_text.split()) < 30:
            return "Text too short to summarize!"
        
        result = self.summarizer(
            long_text, 
            max_length=50, 
            min_length=10
        )
        return result[0]['summary_text']
    
    def mood_check(self, text):
        """Analyze sentiment"""
        result = self.sentiment_analyzer(text)
        sentiment = result[0]
        return f"{sentiment['label']} (confidence: {sentiment['score']:.2f})"
    
    def ask_anything(self, context, question):
        """Answer questions about provided context"""
        result = self.qa_system(question=question, context=context)
        return f"Answer: {result['answer']} (confidence: {result['score']:.2f})"
# Demo script
def demo_toolkit():
    ai = AIToolkit()
    
    print("\n🎪 AI Toolkit Demo")
    
    # Creative writing
    print("\n📝 Creative Writing:")
    story = ai.write_with_me("In a world where developers had superpowers,")
    print(f"Generated: {story}")
    
    # Summarization
    print("\n📄 Summarization:")
    long_text = """
    Artificial intelligence has transformed the software development landscape
    in unprecedented ways. From code generation to automated testing,
    AI tools are becoming integral to the developer workflow. Machine learning
    models can now write documentation, detect bugs, and even suggest
    architectural improvements. The integration of AI into development
    environments has reduced repetitive tasks and increased productivity
    across teams worldwide.
    """
    summary = ai.tldr_this(long_text)
    print(f"TL;DR: {summary}")
    
    # Sentiment analysis
    print("\n😊 Mood Analysis:")
    mood = ai.mood_check("I absolutely love building AI applications!")
    print(f"Sentiment: {mood}")
    
    # Question answering
    print("\n❓ Q&A System:")
    context = "Paris is the capital of France. It's famous for the Eiffel Tower and excellent cuisine."
    answer = ai.ask_anything(context, "What is Paris known for?")
    print(answer)
if __name__ == "__main__":
    demo_toolkit()