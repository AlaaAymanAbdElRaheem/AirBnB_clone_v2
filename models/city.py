#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, db_mode
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if db_mode:
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""
