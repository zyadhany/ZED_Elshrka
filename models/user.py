#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'
    handle = Column(String(64), primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    age = Column(Integer, default=99)
    gender = Column(String(6), default='Eng')
    rate = Column(Integer, default=1000)
    status = Column(String(1024), default="")