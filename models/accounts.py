#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class account(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'accounts'
    saged = Column(String(60), primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    phonenumber = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)

