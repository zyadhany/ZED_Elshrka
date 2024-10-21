#!/usr/bin/python3
"""app"""
from flask import Flask, flash, redirect, render_template, request, session, send_file
from flask import make_response, jsonify
from flask_session import Session
from healper import login_required, ConstVar
from models import storage
from os import getenv
from flask_cors import CORS
from api.v1.application import root_bp
from api.v1.data import app_data


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


app.url_map.strict_slashes = False
app.register_blueprint(app_data, url_prefix='/api')
app.register_blueprint(root_bp, url_prefix='/')

@app.teardown_appcontext
def tear(self):
    ''' closes storage  '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' handle error '''
    return make_response(render_template('404.html'), 404)

if __name__ == '__main__':
    app.run(debug=True)
