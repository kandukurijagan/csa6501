# Prompt Engineering Assignment
# Summarize an article into 50 words

# Sample Article
article = """
Artificial Intelligence (AI) is transforming various industries by automating
tasks, improving decision-making, and enhancing productivity. In healthcare,
AI assists doctors in disease diagnosis, medical imaging, drug discovery,
robotic surgery, and personalized treatment. AI-powered virtual assistants
provide round-the-clock patient support. Although AI offers many advantages,
it also raises concerns regarding data privacy, security, and ethical issues.
Researchers continue to develop AI systems that are more accurate, reliable,
and transparent, making healthcare more efficient and accessible in the future.
"""

# Zero-shot Prompt
zero_shot = f"""
Summarize the following article in exactly 50 words.

Article:
{article}
"""

# One-shot Prompt
one_shot = f"""
Example

Article:
Cloud computing provides online storage and computing services.
It helps businesses reduce costs and improve flexibility.

Summary (50 words):
Cloud computing enables users to access computing resources over the internet.
It reduces infrastructure costs, improves scalability, enhances collaboration,
and supports business continuity. Organizations benefit from flexible services,
efficient data management, and secure storage, making cloud technology an
essential part of modern digital transformation.

Now summarize the following article in exactly 50 words.

Article:
{article}
"""

# Few-shot Prompt
few_shot = f"""
Example 1

Article:
Cybersecurity protects computers and networks from cyber attacks.

Summary:
Cybersecurity safeguards systems, networks, and sensitive information from
digital threats. It uses encryption, authentication, and security tools to
prevent attacks and ensure data privacy.

Example 2

Article:
The Internet of Things connects devices through the internet.

Summary:
IoT enables smart devices to communicate and share information. It improves
automation, efficiency, and monitoring across homes, industries, agriculture,
and healthcare.

Now summarize the following article in exactly 50 words.

Article:
{article}
"""

print("="*70)
print("ZERO-SHOT PROMPT")
print("="*70)
print(zero_shot)

print("="*70)
print("ONE-SHOT PROMPT")
print("="*70)
print(one_shot)

print("="*70)
print("FEW-SHOT PROMPT")
print("="*70)
print(few_shot)

# Sample Generated Summaries
zero_summary = """
Artificial Intelligence improves healthcare through disease diagnosis,
medical imaging, robotic surgery, drug discovery, and personalized treatment.
It also supports patients using virtual assistants. Despite privacy and ethical
challenges, AI continues to improve healthcare efficiency, accuracy, and
accessibility for future medical services.
"""

one_summary = """
Artificial Intelligence enhances healthcare by supporting diagnosis, medical
imaging, robotic surgery, drug discovery, and personalized medicine. Virtual
assistants improve patient care. Although privacy and ethical concerns exist,
AI is becoming more reliable, helping create efficient and accessible
healthcare systems.
"""

few_summary = """
Artificial Intelligence transforms healthcare through accurate diagnosis,
medical imaging, robotic surgery, drug discovery, personalized treatment,
and virtual assistants. While data privacy and ethical issues remain,
continuous AI advancements promise improved efficiency, reliability,
and better healthcare access for everyone.
"""

print("\nGenerated Summaries")
print("-"*70)
print("Zero-shot Summary:\n", zero_summary)
print("\nOne-shot Summary:\n", one_summary)
print("\nFew-shot Summary:\n", few_summary)

print("\nComparison")
print("-"*70)
print("{:<12} {:<12} {:<14} {:<12}".format(
    "Prompt", "Accuracy", "Completeness", "Readability"))
print("-"*70)
print("{:<12} {:<12} {:<14} {:<12}".format(
    "Zero-shot", "Good", "Moderate", "Good"))
print("{:<12} {:<12} {:<14} {:<12}".format(
    "One-shot", "Very Good", "Good", "Very Good"))
print("{:<12} {:<12} {:<14} {:<12}".format(
    "Few-shot", "Excellent", "Excellent", "Excellent"))