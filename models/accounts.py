#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class account(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'accounts'
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user = relationship("User", uselist=False, backref="account") 
