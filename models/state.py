#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            """returns a list of city"""
            citie_s = models.storage.all(City)
            relation_n = []
            for data in citie_s.values():
                if data.state_id == self.id:
                    relation_n.append(data)
            return relation_n
