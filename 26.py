from openai import OpenAI

client = OpenAI(api_key="")

prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print(response.output_text)