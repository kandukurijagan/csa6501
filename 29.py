from google import genai

client = genai.Client(api_key="")

problem = input("Enter the programming problem: ")

prompt = f"""
You are a Python programmer.

Write a Python program for the following problem.

Problem:
{problem}

Requirements:
1. Use functions.
2. Display proper output.
3. Explain the logic.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)