# Prompt Engineering Assignment
# Topic: Professional Leave Email Due to Illness

# -------------------------------
# Zero-shot Prompt
# -------------------------------
zero_shot_prompt = """
Write a professional email requesting one day of leave due to illness.
The email should be polite, formal, and include a subject, reason for leave,
and a request for approval.
"""

# -------------------------------
# One-shot Prompt
# -------------------------------
one_shot_prompt = """
Example:

Task:
Write a professional email requesting leave for a family function.

Email:

Subject: Leave Request for Family Function

Dear Sir/Madam,

I would like to request leave for one day as I need to attend an important
family function. I will complete my pending work before my leave and ensure
there is no delay in my responsibilities.

Kindly approve my leave request.

Thank you.

Yours sincerely,
John

Now write a professional email requesting leave due to illness.
"""

# -------------------------------
# Few-shot Prompt
# -------------------------------
few_shot_prompt = """
Example 1

Task:
Write a leave email for attending a wedding.

Email:

Subject: Leave Request

Dear Sir/Madam,

I request one day leave to attend a family wedding. I have completed my
assigned tasks and will resume work the following day.

Thank you.

Regards,
John

Example 2

Task:
Write a leave email for a medical appointment.

Email:

Subject: Leave Request for Medical Appointment

Dear Sir/Madam,

I request leave for one day to attend a medical appointment. I will complete
my pending work upon my return.

Thank you.

Regards,
John

Now write a professional leave email due to illness.
"""

# -------------------------------
# Display Prompts
# -------------------------------
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

# -------------------------------
# Sample Generated Emails
# -------------------------------

zero_email = """
Subject: Leave Request Due to Illness

Dear Sir/Madam,

I am feeling unwell and request one day of leave today. I will return to work
once I recover and complete any pending tasks.

Kindly approve my leave request.

Thank you.

Yours sincerely,
John
"""

one_email = """
Subject: Sick Leave Request

Dear Sir/Madam,

I am writing to request one day of sick leave as I am suffering from a fever
and have been advised to take rest. I will ensure that my pending work is
completed after I return.

I kindly request your approval.

Thank you for your understanding.

Yours sincerely,
John
"""

few_email = """
Subject: Request for Sick Leave

Dear Sir/Madam,

I hope you are doing well. I am feeling unwell due to illness and my doctor
has advised me to take rest for a day. Therefore, I kindly request one day
of sick leave.

I will catch up on any missed work once I return and ensure all my
responsibilities are completed.

Thank you for your understanding and consideration.

Yours sincerely,
John
"""

print("\n" + "=" * 70)
print("GENERATED EMAILS")
print("=" * 70)

print("\nZero-shot Email:")
print(zero_email)

print("\nOne-shot Email:")
print(one_email)

print("\nFew-shot Email:")
print(few_email)

# -------------------------------
# Comparison
# -------------------------------

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("{:<12} {:<12} {:<12} {:<14} {:<14}".format(
    "Prompt", "Tone", "Grammar", "Formatting", "Completeness"))

print("-" * 70)

print("{:<12} {:<12} {:<12} {:<14} {:<14}".format(
    "Zero-shot", "Good", "Good", "Good", "Moderate"))

print("{:<12} {:<12} {:<12} {:<14} {:<14}".format(
    "One-shot", "Very Good", "Very Good", "Very Good", "Good"))

print("{:<12} {:<12} {:<12} {:<14} {:<14}".format(
    "Few-shot", "Excellent", "Excellent", "Excellent", "Excellent"))