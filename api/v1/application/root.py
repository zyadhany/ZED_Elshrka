from flask import redirect, render_template, session, request
from healper import login_required
from .home import home_bp
from .profile import profile_bp
from .groups import groups_bp
from .contests import contests_bp
from .problems import problems_bp
from .login import login, register
from flask import Blueprint
from healper import login_required, ConstVar, user_profile


root_bp = Blueprint('root_bp', __name__)

root_bp.register_blueprint(home_bp, url_prefix='/home')
root_bp.register_blueprint(profile_bp, url_prefix='/profile')
root_bp.register_blueprint(groups_bp, url_prefix='/groups')
root_bp.register_blueprint(contests_bp, url_prefix='/contests')
root_bp.register_blueprint(problems_bp, url_prefix='/problems')
  
@root_bp.before_request
def before_request_func():
    if request.endpoint not in ConstVar.LOGIN_URL_ENDPOINTS:
        session['last_url_login'] = request.url
        res = login_required()
        if res is not None:
            return (res)
    return

@root_bp.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@root_bp.route("/")
def index():
    return redirect("home/")


@root_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@root_bp.route("register", methods=["GET", "POST"])
def register_route():
    return register()

@root_bp.route("login", methods=["GET", "POST"])
def login_route():
    return login()


