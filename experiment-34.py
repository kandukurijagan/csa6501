!pip install transformers torch

from transformers import pipeline

qa_model = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

context = """
Engineering students study subjects such as programming,
electronics, mechanics, mathematics, artificial intelligence
and communication systems.

Python is widely used for artificial intelligence and machine learning.
A compiler converts source code into machine code.
Ohm's law states that voltage is equal to current multiplied by resistance.
"""

while True:
    question = input("\nAsk an engineering question (type exit to stop): ")

    if question.lower() == "exit":
        break

    answer = qa_model(question=question, context=context)
    print("Answer:", answer["answer"])
