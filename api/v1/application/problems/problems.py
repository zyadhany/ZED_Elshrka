from flask import Blueprint, render_template, abort
from healper import user_profile, Time_left, seconds_to_hms
from models import storage, Problem

problems_bp = Blueprint('problems_bp', __name__)

@problems_bp.route("/")
def problems_route():
    user = user_profile()
    problems = storage.all(Problem)
    problem_list = []
    for problem in problems.values():
        problem_list.append(problem.to_dict())
    return render_template('problems.html', user=user, problems=problem_list)


@problems_bp.route("/<id>")
def problem_id(id):
    return f'Problem {id}'
    if problem is None:
        abort(404)
    