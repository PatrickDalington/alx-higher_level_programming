#!/usr/bin/python3

"""
    this module defines a State class
    that inherits from declarative_base
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        this states class inherits from declarative base
        and defines a State table with columns(id, name)
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
