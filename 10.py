from transformers import pipeline
pipe=pipeline("sentiment-analysis")
print(pipe("I love Python"))