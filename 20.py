from transformers import pipeline
generator=pipeline("text-generation",model="gpt2")
prompts=["AI is","Education will","Python programming"]
for p in prompts:
    print(generator(p,max_length=30,num_return_sequences=1)[0]["generated_text"])