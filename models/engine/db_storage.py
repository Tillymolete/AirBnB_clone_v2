#!usr/bin/python3
"""A new class for sqlalchemy database storage"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """Creates a engine and session tables for the env"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for data base storage"""
        self.__engine =  create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, pwd, host, db),
                pool_pre_ping=True)

        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects"""

        objects = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
                query = self.__session.query(cls)
                for elem in query:
                    key = "{].{}".format(type(elem).__name__, elem.id)
                    objects[key] = elem
        else:
            lists = [State, City, user, Place, Review, amenity]
            for clase in lists:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{]".format(type(elem).__name__, elem.id)
                    objects[key] = obj

        return (objects)

    def new(self, obj):
        """adds a new objects to the database"""
        self.__session.add(obj)

    def save(self):
        """Saves the changes on the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the obj from current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads the database"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
