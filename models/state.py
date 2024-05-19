#!/usr/bin/python3
"""This represents the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """This is the class definition for State.

Attributes:
- name: Input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns a list of City instances with the specified state_id."""
            from models import storage
            from models import City
            return [v for k, v in storage.all(City).items()
                    if v.state_id == self.id]
