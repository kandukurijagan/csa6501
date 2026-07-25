from transformers import pipeline
generator=pipeline("text-generation",model="gpt2")
print(generator("Technology is",max_length=40,num_return_sequences=1))