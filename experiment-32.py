# Prompt Evaluation, Comparison and Refinement

task = "Generate a professional leave request email."

prompts = [
    "Write a leave email.",
    "Write a professional leave email requesting one day leave due to illness.",
    """Write a professional leave email.

Requirements:
1. Subject
2. Greeting
3. Reason for leave
4. Leave date
5. Polite closing
6. Professional tone
"""
]

responses = [
    "I need leave tomorrow because I am sick.",
    
    """Dear Manager,

I am feeling unwell and request one day leave.

Thank you.
""",

    """Subject: Leave Request

Dear Manager,

I am feeling unwell and request one day leave on 2 August 2026.
I will complete my pending work after returning.

Thank you for your understanding.

Sincerely,
Ramesh
"""
]

scores = [
    ["Medium", "Medium", "Low", "Low", "Poor"],
    ["Good", "Good", "Medium", "Good", "Good"],
    ["Excellent", "Excellent", "Excellent", "Excellent", "Excellent"]
]

criteria = ["Relevance", "Accuracy", "Completeness", "Clarity", "Format"]

for i in range(3):
    print("=" * 60)
    print("Prompt", i + 1)
    print("-" * 60)
    print(prompts[i])

    print("\nGenerated Response:")
    print(responses[i])

    print("\nEvaluation")
    for c, s in zip(criteria, scores[i]):
        print(f"{c:<15}: {s}")
    print()

print("=" * 60)
print("Refined Prompt")
print("=" * 60)

refined_prompt = """
You are a professional email writer.

Write a formal leave request email.

Requirements:
• Include Subject.
• Include Greeting.
• Mention the reason.
• Mention leave date.
• Mention work handover.
• Use polite closing.
• Keep within 150 words.
• Output only the email.
"""

print(refined_prompt)
