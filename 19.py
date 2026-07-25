from transformers import pipeline
generator=pipeline("text-generation",model="gpt2")
print(generator("The future of AI",max_length=50,num_return_sequences=1))