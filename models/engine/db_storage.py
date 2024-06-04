#!/usr/bin/python3
"""Module for the DBStorage Class"""

from sqlalchemy import (create_engine)
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {
            "Amenity": Amenity, "City": City,
            "Place": Place, "Review": Review,
            "State": State, "User": User
            }


class DBStorage:
    """the class that will interact with the mysql db"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""

        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the db for all objects depending of the class name

        Args:
            cls (class): The class to look for if None get all

        Returns:
            new_dict (dictionary)
        """

        new_dict = {}
        res = None

        for el in classes:
            if cls is None or classes[el]:
                res = self.__session.query(classes[el]).all()
                for obj in res:
                    k = obj.__class__.name + '.' + obj.id
                    new_dict[k] = obj

        return new_dict

    def new(self, obj):
        """
        Adds an object to the current db session

        Args:
            obj (class): the object to be added
        """

        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current db session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current db session obj if not None

        Args:
            obj (class): the object to be deleted
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all the tables of the db
        """

        Base.metadata.create_all(self.__engine)
        s_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_maker)
        self.__session = Session
