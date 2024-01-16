#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all object or filtered"""
        if cls:
            result = {}
            for key, value in self.__objects.items():
                if key.split('.')[0] == cls.__name__:
                    result[key] = value
            return result
        return self.__objects

    def new(self, obj):
        """Adds new object to storage __objects."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialises objects into JSON"""
        serialized_objects = {k: v.to_dict()
                              for k, v in self.__objects.items()}
        print(serialized_objects)
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Reloads instances from JSON file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def delete(self, obj=None):
        """deletes an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
