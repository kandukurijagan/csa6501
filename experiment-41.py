!pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

job_description = """
We are looking for a software engineer with knowledge of
Python, C++, machine learning, artificial intelligence,
SQL and data structures.
"""

resumes = [
    """
    Candidate A: Python programmer with experience in machine learning,
    artificial intelligence and data analysis.
    """,

    """
    Candidate B: Mechanical engineer with knowledge of CAD,
    manufacturing and automobile design.
    """,

    """
    Candidate C: Software developer skilled in Python, C++,
    SQL, machine learning and data structures.
    """
]

job_embedding = model.encode(
    job_description,
    convert_to_tensor=True
)

scores = []

for i, resume in enumerate(resumes):

    resume_embedding = model.encode(
        resume,
        convert_to_tensor=True
    )

    score = util.cos_sim(
        job_embedding,
        resume_embedding
    ).item()

    scores.append((i + 1, score))

scores.sort(key=lambda x: x[1], reverse=True)

print("\nResume Ranking:")

for rank, (candidate, score) in enumerate(scores, 1):
    print(
        "Rank", rank,
        "- Candidate", candidate,
        "- Score:", round(score, 3)
    )
