#!/usr/bin/python3

"""
    this script contains the class definition of a City
"""


from model_state import State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """
        this script defines a City
        class that maps to the table cities
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
