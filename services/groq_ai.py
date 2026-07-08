import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("MODEL_NAME")


def analyze_resume(resume_text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume and return ONLY valid JSON.

Return this exact structure:

{{
    "ats_score": 0,
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "recommended_roles": [],
    "improvements": []
}}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        response_format={"type": "json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )
