from flask import Blueprint, redirect

home_bp = Blueprint('home_bp', __name__)

@home_bp.route("/")
def index():
    return redirect ("ola")
    return "Home Page"

@home_bp.route("/ola")
def fds():
    return "saged"