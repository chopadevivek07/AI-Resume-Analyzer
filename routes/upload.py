import os

from flask import (
    Blueprint,
    request,
    current_app,
    render_template
)

from werkzeug.utils import secure_filename

from services.parser import extract_text
from services.groq_ai import analyze_resume
from services.ats import calculate_ats_score

upload = Blueprint("upload", __name__)

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@upload.route("/upload", methods=["POST"])
def upload_resume():

    # Check if file exists in request
    if "resume" not in request.files:
        return "No file selected."

    file = request.files["resume"]

    # Check if filename is empty
    if file.filename == "":
        return "No file selected."

    # Allow only PDF
    if not allowed_file(file.filename):
        return "Only PDF files are allowed."

    # Secure filename
    filename = secure_filename(file.filename)

    # Save uploaded file
    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # Extract text from PDF
    resume_text = extract_text(filepath)

    # Calculate ATS Score
    ats_result = calculate_ats_score(resume_text)

    # AI Analysis
    analysis = analyze_resume(resume_text)

    # Render Dashboard
    return render_template(
        "dashboard.html",
        filename=filename,
        ats=ats_result,
        analysis=analysis
    )
