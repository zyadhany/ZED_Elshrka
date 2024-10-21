#!/usr/bin/python3
"""This module to make dp storage"""

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.accounts import account
from models import Group, Contest, Problem, Submission
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
            'users': User, 'accounts' : account,
        }

def ConvertStrCls(st):
    if type(st) == str:
        if st in classes:
            return classes[st]
    return (None)

class DBStorage:
    """This class manages dp storage of hbnb"""
    __engine = None
    __session = None

    def __init__(self):
        """init for dp sttorage"""
        SQLITE_DB_PATH = 'local_database.db'
        self.__engine = create_engine(f'sqlite:///{SQLITE_DB_PATH}',
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        #Base.metadata.drop_all(self.__engine)

    def count(self, cls=None):
        ''' count of objects of class '''
        obj_dict = self.all(cls)
        return len(obj_dict)

    def add(self, cls, dict):
        if type(cls) == str:
            cls = ConvertStrCls(cls)
        if cls not in classes.values():
            return None
        obj = cls(**dict)
        return obj

    def edit(self):
        obj = self.__session.query(account).filter_by(id='9').all()[0]
        obj = self.get(account, 15)
        obj.email = 'test'
        self.save()
        return obj

    def get(self, cls, id):
        ''' gett object by id '''
        # self.reload()
        if type(cls) == str:
            cls = ConvertStrCls(cls)

        objs = self.all(cls)
        
        if not objs or not cls:
            return None
    
        obj_str = cls.__name__ + '.' + str(id)
        for key, val in objs.items():
            if key == obj_str:
                return val
        return None

    def getDict(self, cls, dict):
        """ Get All object of cls that Match dict """
        if type(cls) == str:
            cls = ConvertStrCls(cls)
        if cls not in classes.values():
            return None
        objs = self.__session.query(cls).filter_by(**dict).all()
        return (objs)
    
    def delete(self, obj=None):
        """delete object from storage"""
        if obj is None:
            return
        self.__session.delete(obj)

    def close(self):
        """ deserializing the JSON file to objects """
        self.__session.remove()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if type(cls) == str:
            cls = ConvertStrCls(cls)
        
        res = {}
        if cls is None:
            cls = classes.values()
        else:
            cls = [cls]
        for ind in cls:
            if ind not in classes.values():
                continue
            que = self.__session.query(ind).all()
            for obj in que:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                res[key] = obj
        return (res)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(expire_on_commit=False,
                           bind=self.__engine)
        Session = scoped_session(ses)
        self.__session = Session
