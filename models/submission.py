#!/usr/bin/python3
""" Submission Module for managing submissions """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, INTEGER, DateTime, ForeignKey
from sqlalchemy import Index, engine
from sqlalchemy.orm import relationship
from models import User

class Submission(BaseModel, Base):
    """This class represents a submission"""
    __tablename__ = 'submissions'
    
    status = Column(String(50), nullable=False, default='pending')
    time_submitted = Column(DateTime)
    code = Column(String(4096), nullable=False)
    solution_size = Column(INTEGER)
    compiler = Column(String(50))
    execution_time = Column(INTEGER)
    user_handle = Column(String(64), ForeignKey('users.handle'), nullable=False)
    problem_id = Column(INTEGER, ForeignKey('problems.id'), nullable=False)
    problem = relationship("Problem", back_populates="submissions")
    Index('users_handle_idx', User.handle)