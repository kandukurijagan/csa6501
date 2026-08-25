!pip install transformers sentencepiece torch

from transformers import pipeline

translator = pipeline(
    "translation_en_to_hi",
    model="Helsinki-NLP/opus-mt-en-hi"
)

text = input("Enter English engineering text:\n")

result = translator(text)

print("\nHindi Translation:")
print(result[0]["translation_text"])
