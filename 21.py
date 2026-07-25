# Zero-shot Prompt
zero_shot_prompt = """
Write an attractive product description for a Smart Fitness Watch.
Highlight its features, benefits, and target audience.
"""

zero_shot_output = """
Stay active and connected with the Smart Fitness Watch. Track your heart rate,
steps, calories burned, sleep quality, and workouts in real time. With a sleek
design, water resistance, long battery life, and smartphone notifications,
it is the perfect companion for a healthy lifestyle.
"""

# One-shot Prompt
one_shot_prompt = """
Example:

Product: Wireless Bluetooth Earbuds

Description:
Enjoy crystal-clear sound with Wireless Bluetooth Earbuds featuring active
noise cancellation, long battery life, and a comfortable ergonomic design.

Now write a similar product description for:

Product: Smart Fitness Watch
"""

one_shot_output = """
Achieve your fitness goals with the Smart Fitness Watch. Featuring heart rate
monitoring, blood oxygen tracking, sleep analysis, GPS, and multiple sports
modes, this stylish smartwatch keeps you informed and motivated throughout
the day.
"""

# Few-shot Prompt
few_shot_prompt = """
Example 1

Product: Wireless Bluetooth Earbuds

Description:
Experience immersive sound with active noise cancellation and up to 30 hours
of battery life.

Example 2

Product: Portable Power Bank

Description:
Charge your devices anytime with a compact 20,000mAh power bank featuring
fast charging and dual USB ports.

Now write a product description for:

Product: Smart Fitness Watch
"""

few_shot_output = """
Transform your fitness journey with the Smart Fitness Watch. Equipped with
heart rate monitoring, SpO₂ tracking, sleep monitoring, GPS, water resistance,
and smart notifications, it helps you stay healthy while keeping you connected.
Its elegant design and long-lasting battery make it perfect for everyday use.
"""

print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_shot_prompt)
print("Generated Description:")
print(zero_shot_output)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_shot_prompt)
print("Generated Description:")
print(one_shot_output)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_shot_prompt)
print("Generated Description:")
print(few_shot_output)