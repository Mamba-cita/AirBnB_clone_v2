#!/usr/bin/python3
"""This represents the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """This is the class definition for City.

Attributes:
- state_id: The state ID
- name: Input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    places = relationship(
        "Place",
        cascade="all, delete",
        backref=backref("cities", cascade="all"),
        passive_deletes=True)
