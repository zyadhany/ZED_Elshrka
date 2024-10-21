#!/usr/bin/python3
"""This api module """
from flask import Blueprint

app_data = Blueprint('app_data', __name__)

if app_data is not None:
    from .main import *

