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
import os


class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """"Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, file, indent=4)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    class_name = v['__class__']
                    obj = eval(class_name)(**v)
                    self.__objects[k] = obj
