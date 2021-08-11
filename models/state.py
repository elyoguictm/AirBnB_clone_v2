#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship('City', backref="state",
                              cascade="all, delete-orphan")

    if (getenv("HBNB_TYPE_STORAGE") == "file"):
        @property
        def cities(self):
            from models import storage
            from models.city import City
            mycities = {}
            for city, value in storage.all(City).items():
                if (value.state_id == self.id):
                        mycities.update({city: value})
            return mycities
