#!/usr/bin/python3
"""This module instantiates an object of class dp"""

from .accounts import account
from .user import User
from .groups import Group
from .contests import Contest
from .problem import Problem
from .submission import Submission
from models.engine.db_storage import DBStorage
storage = DBStorage()

storage.reload()
