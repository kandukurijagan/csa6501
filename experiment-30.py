# SQL Query Generation using Structured Prompting

prompt = """
You are an SQL expert.

Database Schema:
Table: Student
-----------------------------------------
RollNo      INT
Name        VARCHAR(50)
Department  VARCHAR(20)
Marks       INT
Age         INT
-----------------------------------------

Task:
Generate an SQL query to display the names and marks of students
whose marks are greater than 80.

Output only the SQL query.
"""

print("Structured Prompt:\n")
print(prompt)

# Simulated LLM Response
sql_query = """
SELECT Name, Marks
FROM Student
WHERE Marks > 80;
"""

print("\nGenerated SQL Query:\n")
print(sql_query)
