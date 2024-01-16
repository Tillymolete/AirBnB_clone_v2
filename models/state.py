#!/usr/bin/python3
""" State class for bnb """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Represent  class for state"""
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """return the list of city instances"""

        cities = list()

        for _id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                cities.append(city)
        return cities
