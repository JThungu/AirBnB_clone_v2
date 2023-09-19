#!/usr/bin/python3
""" Describes Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ Describes Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
