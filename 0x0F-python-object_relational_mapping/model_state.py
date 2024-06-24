#!/usr/bin/python3
"""
this is a code to take in data from mysql
using SQLalcamey
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """creates an mysql table
    - Inherits from Base
    - Links to the MySQL table 'states'
    - Contains columns id and name
    Args:
        Base (class): for
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
