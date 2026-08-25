!pip install transformers torch

from transformers import pipeline

chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

print("Engineering College AI Chatbot")
print("Type 'exit' to stop\n")

while True:
    question = input("Student: ")

    if question.lower() == "exit":
        break

    prompt = f"""
    You are an AI assistant for an engineering college.
    Answer the following student question clearly and briefly.

    Question: {question}
    """

    result = chatbot(prompt, max_new_tokens=100)
    print("Bot:", result[0]["generated_text"])
