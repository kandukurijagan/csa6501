import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = input("Enter Prompt: ")

response = model.generate_content(prompt)

print("\nGenerated Response:\n")
print(response.text)
