import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

SECRET_KEY = "resume-analyzer-secret-key"

MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
