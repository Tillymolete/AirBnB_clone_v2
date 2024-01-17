#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel):
    """ The city class
    Attributes:
        state_id: the state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('state_id'), nullable=False)
    name = Column(String(128), nullable=False)
