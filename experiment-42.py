!pip install transformers torch sentencepiece

from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

topic = input("Enter research topic: ")

keyword_prompt = f"""
Generate 8 important research keywords for:
{topic}
"""

info_prompt = f"""
Provide relevant information about the research topic:
{topic}
Explain it clearly for an engineering student.
"""

summary_prompt = f"""
Write a short and meaningful research summary about:
{topic}
"""

keywords = generator(
    keyword_prompt,
    max_new_tokens=100
)

information = generator(
    info_prompt,
    max_new_tokens=200
)

summary = generator(
    summary_prompt,
    max_new_tokens=100
)

print("\nRESEARCH TOPIC:")
print(topic)

print("\nKEYWORDS:")
print(keywords[0]["generated_text"])

print("\nRELEVANT INFORMATION:")
print(information[0]["generated_text"])

print("\nCONCISE SUMMARY:")
print(summary[0]["generated_text"])
