from google import genai

client = genai.Client(api_key="")

topic = input("Enter a topic: ")

prompts = [
    f"Explain {topic}.",
    f"Explain {topic} in simple language with bullet points.",
    f"Explain {topic} with definition, features, advantages, disadvantages, applications and conclusion."
]

for i in range(len(prompts)):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompts[i]
    )
    print("\nPrompt", i + 1)
    print(response.text)

print("\nEvaluation")
print("Prompt 1: Simple explanation")
print("Prompt 2: Better clarity")
print("Prompt 3: Most detailed and complete")
print("Best Prompt: Prompt 3")