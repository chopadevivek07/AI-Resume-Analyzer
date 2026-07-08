import re

SKILLS = [
    "aws",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "linux",
    "python",
    "git",
    "ansible",
    "mysql",
    "mongodb",
    "prometheus",
    "grafana",
    "nginx",
    "flask"
]


def calculate_ats_score(text):

    text = text.lower()

    score = 0

    breakdown = {}

    skills_found = []

    # Contact
    contact = 0

    if re.search(r'[\w\.-]+@[\w\.-]+', text):
        contact += 5

    if re.search(r'\+?\d[\d\s-]{9,14}', text):
        contact += 5

    breakdown["Contact"] = contact
    score += contact

    # Education
    education = 0

    education_keywords = [
        "bca",
        "bachelor",
        "mca",
        "master",
        "education"
    ]

    if any(word in text for word in education_keywords):
        education = 10

    breakdown["Education"] = education
    score += education

    # Skills
    skill_score = 0

    for skill in SKILLS:

        if skill in text:
            skills_found.append(skill)
            skill_score += 2

    if skill_score > 20:
        skill_score = 20

    breakdown["Skills"] = skill_score
    score += skill_score

    # Projects
    project = 20 if "project" in text else 0
    breakdown["Projects"] = project
    score += project

    # Experience
    experience = 20 if (
        "experience" in text or
        "intern" in text
    ) else 0

    breakdown["Experience"] = experience
    score += experience

    # Certification
    certification = 10 if (
        "certification" in text or
        "certifications" in text
    ) else 0

    breakdown["Certification"] = certification
    score += certification

    # Formatting
    formatting = 10
    breakdown["Formatting"] = formatting
    score += formatting

    if score > 100:
        score = 100

    return {
        "score": score,
        "breakdown": breakdown,
        "skills_found": skills_found
    }
