import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"
}

prompt = input("Enter your prompt: ")

response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt}
)

print(response.json()[0]["generated_text"])