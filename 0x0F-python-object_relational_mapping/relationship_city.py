#!/usr/bin/python3
"""
This is a script that defines a City class
to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): Table name of the class
        id (int): id of class
        name (str): Name of class
        state_id (int): State the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
