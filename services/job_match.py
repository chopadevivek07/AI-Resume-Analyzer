import re

SKILLS = [
    "aws","ec2","s3","iam","vpc","rds","lambda",
    "docker","docker compose","kubernetes","helm",
    "terraform","ansible","jenkins","linux","nginx",
    "apache","python","bash","git","github","gitlab",
    "bitbucket","mysql","mongodb","dynamodb",
    "prometheus","grafana","cloudwatch","ci/cd","devops"
]


def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:

        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)

    return sorted(set(found))


def calculate_job_match(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = sorted(list(set(resume_skills) & set(job_skills)))
    missing = sorted(list(set(job_skills) - set(resume_skills)))

    total = len(job_skills)

    if total == 0:
        score = 0
    else:
        score = round((len(matched) / total) * 100)

    if score >= 90:
        recommendation = "Excellent Match 🚀"

    elif score >= 75:
        recommendation = "Good Match 👍"

    elif score >= 60:
        recommendation = "Average Match"

    else:
        recommendation = "Needs Improvement"

    suggestions = []

    if missing:
        suggestions.append(
            f"Learn these missing skills: {', '.join(missing)}"
        )

    suggestions.append("Add measurable achievements using numbers.")
    suggestions.append("Tailor your resume for each job description.")
    suggestions.append("Highlight DevOps and Cloud projects.")
    suggestions.append("Keep GitHub and LinkedIn updated.")

    return {

        "score": score,

        "matched": matched,

        "missing": missing,

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "resume_skill_count": len(resume_skills),

        "job_skill_count": len(job_skills),

        "matched_count": len(matched),

        "missing_count": len(missing),

        "recommendation": recommendation,

        "suggestions": suggestions,

    }
