from flask import Blueprint, render_template

analyze = Blueprint("analyze", __name__)

@analyze.route("/result")
def result():
    return render_template("result.html")
