#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    if models.storage_type == 'db':
        id = Column(Integer, primary_key=True,
                    autoincrement=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = self.cnvrt_to_dt(kwargs['updated_at'])
            else:
                self.updated_at = datetime.now()

            if 'created_at' in kwargs:
                kwargs['created_at'] = self.cnvrt_to_dt(kwargs['created_at'])
            else:
                self.created_at = datetime.now()

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)

        # storage.new(self)

    @staticmethod
    def cnvrt_to_dt(str):
        """Convert a string to a datetime object

        Args:
            str: String to convert

        Returns:
            datetime: Datetime object
        """
        return datetime.strptime(str, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if dictionary[_sa_instance_state]:
            del dictionary[_sa_instance_state]

        return dictionary
