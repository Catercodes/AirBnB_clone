#!/usr/bin/python3
import uuid
from datetime import datetime
from datetime import time


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Assigning them to the right values"""
        # self.id = str(uuid.uuid4())
        # self.created_at = datetime.now()
        # self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':

                    if key in ['updated_at', 'created_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)

        else:
            # Generate a unique ID and convert to string
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage

            storage.new(self)

    def __str__(self):
        """ returns the string format of the above"""
        _str = "[{:s}] ({:s}) {:s}"
        _str = _str.format(
            self.__class__.__name__, self.id, str(
                self.__dict__))
        return _str

    def save(self):
        """ update attr to the current time"""
        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """ return the dict  format for  the above """
        dcopy = self.__dict__.copy()
        dcopy["__class__"] = self.__class__.__name__
        dcopy["created_at"] = self.created_at.isoformat()
        dcopy["updated_at"] = self.updated_at.isoformat()
        return dcopy
