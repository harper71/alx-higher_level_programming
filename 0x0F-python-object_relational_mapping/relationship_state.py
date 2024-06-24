#!/usr/bin/python3
"""
This module contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    """
    State class:
    - Inherits from Base
    - Links to the MySQL table 'states'
    - Contains columns id and name
    - Has a one-to-many relationship with City objects
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    # Define the one-to-many relationship with City
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
