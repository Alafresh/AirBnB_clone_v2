#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
import models

place_amenity = Table(
                'place_amenity', Base.metada,
                Column('place_id', String(60), ForeignKey('places.id')),
                Column('amenity_id', String(60), ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="delete", backref="places")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="places", viewonly=False)
    else:
        @property
        def reviews(self):
            """returns a list of city"""
            reviews_s = models.storage.all(Review)
            relation_n = []
            for data in reviews_s.values():
                if data.state_id == self.id:
                    relation_n = relation_n.append(data)
            return relation_n

        @property
        def amenities(self):
            """ Relation between amenity and place"""
            ameni = models.storage.all(Amenity)
            ameni_relation = []
            for amenity in ameni.values():
                if amenity.id == self.amenity_ids:
                    ameni_relation = ameni_relation.append(amenity)
            return ameni_relation

        @amenities.setter
        def amenities(self, ameni_id):
            """ id for a places """
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id == ameni_id:
                    self.amenity_ids.append(ameni_id)
