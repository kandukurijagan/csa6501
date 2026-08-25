
task = "Translate 'Good Morning' into French."

# Zero-shot Prompt
zero_shot_prompt = f"""
Task:
{task}
"""

zero_shot_response = "Bonjour"

# One-shot Prompt
one_shot_prompt = """
Example:
English: Thank You
French : Merci

Now Translate:
English: Good Morning
French:
"""

one_shot_response = "Bonjour"

# Few-shot Prompt
few_shot_prompt = """
Example 1:
English: Hello
French : Bonjour

Example 2:
English: Thank You
French : Merci

Example 3:
English: Good Night
French : Bonne Nuit

Now Translate:
English: Good Morning
French:
"""

few_shot_response = "Bonjour"

print("========== ZERO-SHOT ==========")
print(zero_shot_prompt)
print("Response:", zero_shot_response)

print("\n========== ONE-SHOT ==========")
print(one_shot_prompt)
print("Response:", one_shot_response)

print("\n========== FEW-SHOT ==========")
print(few_shot_prompt)
print("Response:", few_shot_response)

print("\n========== COMPARISON ==========")
print("{:<12} {:<12} {:<12} {:<12}".format(
    "Technique", "Accuracy", "Quality", "Consistency"))

print("{:<12} {:<12} {:<12} {:<12}".format(
    "Zero-shot", "Medium", "Good", "Medium"))

print("{:<12} {:<12} {:<12} {:<12}".format(
    "One-shot", "High", "Better", "High"))

print("{:<12} {:<12} {:<12} {:<12}".format(
    "Few-shot", "Very High", "Excellent", "Very High"))
