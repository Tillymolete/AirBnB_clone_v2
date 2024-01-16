#!/usr/bin/python3
"""This is a Db storgae class"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review}


class DBStorage:
    """interacts with a mysql database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instances of a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        result = {}
        for cls in classes:
            if cls is None or cls is classes[cls] or cls is cls:
                objs = self.__session.query(classes[cls]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    result[key] = obj
            return (result)

    def new(self, obj):
        """adds the object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current databse obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
