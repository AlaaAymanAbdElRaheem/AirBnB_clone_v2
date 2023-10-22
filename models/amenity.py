#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, db_mode
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ The Amenity class """
    if db_mode:
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False,
                                       overlaps="place_amenities")
    else:
        name = ""
