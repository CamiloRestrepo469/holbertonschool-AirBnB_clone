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
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists;
        otherwise, do nothing. If the file doesn't exist, no exception
        should be raised).
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals().get(class_name)
                    if class_name in self.classe:
                        class_obj = self.classe[class_name]
                        instance = class_obj(**value)
                        self.new(instance)
        except AttributeError:
            pass
       