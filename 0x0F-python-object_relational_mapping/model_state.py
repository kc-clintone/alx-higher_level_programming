#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

bse = declarative_base()


class State(bse):
    """
    The state class
    Attributes:
        __tablename__ (str): Table name of the class
        id (int): State id of the class
        name (str): State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
