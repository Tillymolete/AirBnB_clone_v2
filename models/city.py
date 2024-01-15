#!/usr/bin/python3
""" City class for HBNB project """
import models
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel):
    """ The city class, which represents city """
    if models.storage_type == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
