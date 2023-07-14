#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.user import User
from datetime import datetime

class FileStorage:
    
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
            
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file-path, 'r') as file:
                data = json.load(file)
            for key in data: self.classes[data[key]["__class__"]](**data[key])
        except AttributeError:
            pass
       