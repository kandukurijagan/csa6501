from openai import OpenAI

# Replace with your API Key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print("\nGenerated Text:\n")
print(response.output_text)
