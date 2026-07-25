# Prompt Engineering Assignment
# Topic: Promotional Social Media Post for an AI Workshop

# -------------------------------------
# Zero-shot Prompt
# -------------------------------------
zero_shot_prompt = """
Create a promotional social media post for an AI Workshop.

Requirements:
- Mention the workshop title.
- Highlight AI learning opportunities.
- Encourage people to register.
- Keep the tone exciting and professional.
"""

# -------------------------------------
# One-shot Prompt
# -------------------------------------
one_shot_prompt = """
Example:

Event: Web Development Bootcamp

Post:
🚀 Join our Web Development Bootcamp!
Learn HTML, CSS, JavaScript, and React from industry experts.
📅 Date: 20 August
📍 Venue: ABC College
🎯 Register now to kickstart your web development career!

Now create a similar promotional post for an AI Workshop.
"""

# -------------------------------------
# Few-shot Prompt
# -------------------------------------
few_shot_prompt = """
Example 1

Event: Cybersecurity Seminar

Post:
🔒 Protect Your Future with Cybersecurity!
Join our expert-led seminar to learn ethical hacking,
network security, and cyber defense strategies.
Register today!

Example 2

Event: Data Science Workshop

Post:
📊 Become a Data Science Expert!
Learn Python, Machine Learning, and Data Visualization
through hands-on sessions.
Limited seats available—Register Now!

Now create a promotional social media post for an AI Workshop.
"""

# -------------------------------------
# Display Prompts
# -------------------------------------
print("=" * 70)
print("ZERO-SHOT PROMPT")
print("=" * 70)
print(zero_shot_prompt)

print("\n" + "=" * 70)
print("ONE-SHOT PROMPT")
print("=" * 70)
print(one_shot_prompt)

print("\n" + "=" * 70)
print("FEW-SHOT PROMPT")
print("=" * 70)
print(few_shot_prompt)

# -------------------------------------
# Sample Generated Posts
# -------------------------------------

zero_post = """
🤖 AI Workshop

Join our AI Workshop to explore Artificial Intelligence,
Machine Learning, and real-world AI applications.
Learn from experts and gain practical experience.

📅 Date: 15 September
📍 Venue: ABC College

Register Now!
"""

one_post = """
🚀 AI Workshop 2026

Ready to explore the future of Artificial Intelligence?
Join our AI Workshop and learn Machine Learning,
Deep Learning, and Generative AI through hands-on sessions.

📅 Date: 15 September
📍 Venue: ABC College
🎓 Certificate Provided

Register Today!
"""

few_post = """
🌟 AI Workshop – Learn the Future of Technology!

Discover Artificial Intelligence, Machine Learning,
Deep Learning, ChatGPT, and Computer Vision through
interactive sessions led by industry experts.

📅 Date: 15 September
📍 Venue: ABC College
🎓 Certificate of Participation
💻 Hands-on Projects
📢 Limited Seats Available!

👉 Register Now and Start Your AI Journey!
"""

print("\n" + "=" * 70)
print("GENERATED SOCIAL MEDIA POSTS")
print("=" * 70)

print("\nZero-shot Post:")
print(zero_post)

print("\nOne-shot Post:")
print(one_post)

print("\nFew-shot Post:")
print(few_post)

# -------------------------------------
# Comparison
# -------------------------------------

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
    "Prompt", "Creativity", "Clarity", "Engagement", "Completeness"))

print("-" * 75)

print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
    "Zero-shot", "Good", "Good", "Moderate", "Good"))

print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
    "One-shot", "Very Good", "Very Good", "Good", "Very Good"))

print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
    "Few-shot", "Excellent", "Excellent", "Excellent", "Excellent"))