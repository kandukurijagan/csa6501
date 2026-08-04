from google import genai

client = genai.Client(api_key="")

schema = """
Employee(
EmpID,
Name,
Department,
Salary
)
"""

task = input("Enter your SQL requirement: ")

prompt = f"""
Database Schema:
{schema}

Requirement:
{task}

Generate only the SQL query.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)