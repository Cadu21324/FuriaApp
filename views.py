from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def homepage():
    return render_template("index.html")
