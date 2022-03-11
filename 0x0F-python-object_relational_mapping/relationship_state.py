#!/usr/bin/python3
""" Module to connect to mysql with SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sys

Base = declarative_base()


class State(Base):
    """ Database table model"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")
