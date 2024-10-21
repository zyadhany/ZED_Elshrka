from flask import Blueprint, render_template
from .contest import contest_bp
from healper import user_profile
from models import storage, Group

groups_bp = Blueprint('groups_bp', __name__)
groups_bp.register_blueprint(contest_bp, url_prefix='/contest')

@groups_bp.route("/", methods=["POST"])
def TT():
    user = user_profile()
    groups = storage.all(Group)
    group_list = []
    for group in groups.values():
        group_list.append(group.to_dict())
    return render_template('group.html', user=user, groups=group_list)

@groups_bp.route("/")
def index():
    user = user_profile()
    groups = storage.all(Group)
    group_list = []
    for group in groups.values():
        group_list.append(group.to_dict())
    return render_template('group.html', user=user, groups=group_list)

