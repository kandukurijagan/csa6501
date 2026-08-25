import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"
}

prompt = input("Enter Prompt: ")

payload = {
    "inputs": prompt
}

response = requests.post(API_URL, headers=headers, json=payload)

print("\nGenerated Text:\n")
print(response.json())
