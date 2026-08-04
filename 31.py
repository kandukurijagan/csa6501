from google import genai

client = genai.Client(api_key="")

task = input("Enter a task: ")

zero = task

one = f"""
Example

Input:
Explain AI

Output:
Artificial Intelligence enables machines to perform tasks that normally require human intelligence.

Task:
{task}
"""

few = f"""
Example 1

Input:
Explain AI

Output:
AI enables computers to imitate human intelligence.

Example 2

Input:
Explain Machine Learning

Output:
Machine Learning is a branch of AI where computers learn from data.

Task:
{task}
"""

r1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=zero
)

r2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=one
)

r3 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=few
)

print("Zero-shot Response\n")
print(r1.text)

print("\nOne-shot Response\n")
print(r2.text)

print("\nFew-shot Response\n")
print(r3.text)