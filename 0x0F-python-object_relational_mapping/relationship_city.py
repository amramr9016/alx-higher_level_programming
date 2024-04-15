#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id_num (int): The id of the class
        city_name (str): The name of the class
        state_id_num (int): The state the city belongs to
    """
    __tablename__ = 'cities'

    id_num = Column(Integer, primary_key=True)
    city_name = Column(String(128), nullable=False)
    state_id_num = Column(Integer, ForeignKey('states.id'), nullable=False)
