from flask import Blueprint, render_template, request
from services.job_match import calculate_job_match

job_match = Blueprint("job_match", __name__)


@job_match.route("/job-match", methods=["GET", "POST"])
def job_match_page():

    if request.method == "POST":

        resume_text = request.form.get("resume_text", "")
        job_description = request.form.get("job_description", "")

        result = calculate_job_match(resume_text, job_description)

        return render_template(
            "job_match_result.html",
            result=result,
            resume_text=resume_text,
            job_description=job_description
        )

    return render_template("job_match.html")
