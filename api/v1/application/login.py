from flask import redirect, render_template, session, request
from healper import login_post, register_post

def register():
    if request.method == "POST":
        status = register_post(request.form)
        if status is not None:
            return render_template("register.html", message=status)
        return redirect("/")
        
    return render_template("register.html") 


def login():
    session.clear()
    if request.method == "POST":
        handle = login_post(request.form)
        # error massage if can't login
        if handle is None:
            return render_template("login.html", message="invalid username and/or password.")
        session["handle"] = handle
        return redirect("/")

    return render_template("login.html") 
