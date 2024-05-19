#!/usr/bin/python3
"""This serves as the foundational model class for AirBnB."""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """This class defines all shared attributes and methods applicable to other classes.
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of the base model class.

        Parameters:
            - args: not utilized
            - kwargs: arguments for the constructor of the BaseModel

        Attributes:
            - id: a unique identifier generated
            - created_at: date of creation
            - updated_at: date of last update
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            # TODO: wtf? more error checking?
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string.

Return:
- A string containing the class name, id, and a dictionary representation.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

    def __repr__(self):
        """Returns a string representation.
        """
        return self.__str__()

    def save(self):
        """Updates the public instance attribute `updated_at` to the current timestamp.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary of the class and returns it.

Return:
- A dictionary containing all the key-value pairs in the `__dict__` attribute.
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """Deletes the current instance from the storage (models.storage)."""
        models.storage.delete(self)
