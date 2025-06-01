from transformers import pipeline

# This felt like magic
generator = pipeline("text-generation", model="gpt2")

# My test
prompt = "The best thing about being a developer is"
result = generator(prompt, max_length=50)
print(result[0]['generated_text'])