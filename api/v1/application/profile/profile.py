from flask import Blueprint, redirect, render_template, request, abort
from healper import login_required, user_profile
import requests
import time

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route("/", methods=["GET", "POST"])
def index():
    user = user_profile()
    if request.method == "POST":
        url = 'http://127.0.0.1:5000/api/gen/users'
        payload = {
            'info': {'handle': user['handle']},
            'attach': request.form.to_dict()
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.request('PUT', url, json=payload, headers=headers)
        if response.status_code != 200:
            abort(404)
        return redirect('./')
    return render_template('profile.html', user=user)



@profile_bp.route("/<username>")
def profile(username):
    return ("Hello " + username)

