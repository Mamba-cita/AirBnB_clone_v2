#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    reviews = relationship('Review', cascade='all, delete', backref='user')


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            """ Getter attribute for reviews """
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
