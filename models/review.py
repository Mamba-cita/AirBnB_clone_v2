#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from models.base_model import Base
from os import getenv

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # Define additional properties/methods specific to the database storage
        pass
    else:
        # Define additional properties/methods specific to the file storage
        pass
