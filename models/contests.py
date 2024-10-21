#!/usr/bin/python3
""" Contest Module for managing contests """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Contest(BaseModel, Base):
    """This class represents a contest"""
    __tablename__ = 'contests'
    
    duration = Column(Integer, nullable=False, default=10)
    contest_name = Column(String(32), nullable=False)
    contest_level = Column(Integer)
    start_time = Column(DateTime)
    group_id = Column(Integer, ForeignKey('group_contest.id'), nullable=False)
    group = relationship("Group", back_populates="contests")
    problems = relationship("Problem", back_populates="contest")
