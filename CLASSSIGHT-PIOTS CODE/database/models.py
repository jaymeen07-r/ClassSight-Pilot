"""
SQLAlchemy ORM Models

Defines database schema for all entities.
"""

from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    """User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    full_name = Column(String(255))
    role = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    students = relationship("Student", back_populates="parent")
    
    def __repr__(self):
        return f"<User(email={self.email}, role={self.role})>"


class Student(Base):
    """Student model."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(String(50), unique=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    class_assigned = Column(String(50))
    parent_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(
