# ==========================================
# Prompt Engineering Assignment
# Topic: Applications of Artificial Intelligence in Healthcare
# ==========================================

# Zero-shot Prompt
zero_shot = """
Write a 200-word blog on "Applications of Artificial Intelligence in Healthcare."

Instructions:
- Include a suitable title.
- Explain how AI is transforming healthcare.
- Mention disease diagnosis, medical imaging, robotic surgery,
  drug discovery, personalized medicine, and virtual assistants.
- End with a short conclusion.
"""

# One-shot Prompt
one_shot = """
Example

Topic: Cloud Computing

Blog:
Cloud computing allows users to store and access data over the internet.
It offers flexibility, scalability, and cost savings for businesses.
Cloud services improve collaboration, ensure data backup, and support
digital transformation.

Now write a 200-word blog on:

Topic: Applications of Artificial Intelligence in Healthcare
"""

# Few-shot Prompt
few_shot = """
Example 1

Topic: Internet of Things (IoT)

Blog:
The Internet of Things connects devices through the internet,
allowing them to communicate and exchange information.
IoT is widely used in smart homes, industries, agriculture,
and healthcare.

Example 2

Topic: Cybersecurity

Blog:
Cybersecurity protects computers, networks, and data from
online threats. Strong security practices help prevent
data theft, malware attacks, and unauthorized access.

Now write a 200-word blog on:

Topic: Applications of Artificial Intelligence in Healthcare
"""

print("=" * 70)
print("ZERO-SHOT PROMPT")
print("=" * 70)
print(zero_shot)

print("\n" + "=" * 70)
print("ONE-SHOT PROMPT")
print("=" * 70)
print(one_shot)

print("\n" + "=" * 70)
print("FEW-SHOT PROMPT")
print("=" * 70)
print(few_shot)