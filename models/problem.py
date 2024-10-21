#!/usr/bin/python3
""" Problem Module for managing problems """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Problem(BaseModel, Base):
    """This class represents a problem"""
    __tablename__ = 'problems'
    
    name = Column(String(255), nullable=False)
    rate = Column(Integer, nullable=False)
    contest_id = Column(Integer, ForeignKey('contests.id'))
    contest = relationship("Contest", back_populates="problems")
    submissions = relationship("Submission", back_populates="problem")
