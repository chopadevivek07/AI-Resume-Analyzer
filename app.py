from routes.job_match import job_match
from routes.analyze import analyze
from routes.upload import upload
from flask import Flask
from config.settings import *
from routes.home import home

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

app.register_blueprint(home)
app.register_blueprint(upload)
app.register_blueprint(analyze)
app.register_blueprint(job_match)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
