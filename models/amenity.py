#!/usr/bin/python3
"""class for amenity for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """representation of class amenity"""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialises amenity class"""
        super().__init__(*args, **kwargs)
