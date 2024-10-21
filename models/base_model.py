#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if __class__ in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """delete obj from storage"""
        models.storage.delete(self)
        models.storage.save()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = str(type(self).__name__)
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary
