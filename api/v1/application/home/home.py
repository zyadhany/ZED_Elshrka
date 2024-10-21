from flask import Blueprint, redirect, render_template
from healper import user_profile

home_bp = Blueprint('home_bp', __name__)

@home_bp.route("/", strict_slashes=False)
def index():
    user = user_profile()
    return render_template("index.html", user=user) 

