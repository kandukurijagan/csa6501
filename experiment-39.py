!pip install transformers torch sentencepiece

from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

document = input("Enter the engineering document:\n")

result = summarizer(
    document,
    max_length=100,
    min_length=30,
    do_sample=False
)

print("\nSummary:")
print(result[0]["summary_text"])
