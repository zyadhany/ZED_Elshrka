#!/usr/bin/python3
""" Contest Module for managing contests """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Group(BaseModel, Base):
    """This class represents a contest"""
    __tablename__ = 'group_contest'
    
    name = Column(String(32))
    star = Column(Integer)
    contests = relationship("Contest", back_populates="group")
