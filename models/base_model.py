#!/usr/bin/python3

import uuid
from datetime import datetime
from datetime import timedelta
import models

"""
BaseModel that defines all common attributes/methods for other classes
"""

class BaseModel():
    """Base class for all other models."""

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """
            Args:
                *args: Not used.
                **kwargs: A dictionary of attribute names and values.
        """

        if kwargs:
            for attribute, value in kwargs.items():
                if attribute == 'created_at' or attribute == 'updated_at':
                    setattr(self, attribute, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                if attribute != '__class__':
                    setattr(self, attribute, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"<{self.__dict__}>"
        )

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dict_ = self.__dict__.copy()

        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()

        return dict_
