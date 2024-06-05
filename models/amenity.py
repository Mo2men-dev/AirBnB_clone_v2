#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Amenity(BaseModel):
    """ The Amenity class """
    if models.storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Inits the Amenity class"""
        super().__init__(*args, **kwargs)
