#!/usr/bin/python3
"""Create a Class HBNBCommand"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from typing import Tuple, Optional
import inspect
import shlex

class_names_str = [
    "BaseModel", "User"
    ]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    """Command-line interface for the AIRBNB project."""
    
    classe = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}


    # intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args: str) -> bool:
        """
        Handle the end-of-file event (Ctrl+D).
        """
        return True

    def do_create(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line in self.classe.keys():
            new_instance = self.classe[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] in self.classe.keys():
                if len(tokens) == 1:
                    print("** instance id missing **")
                else:
                    objects = storage.all()
                    flag = None
                    for key in objects.keys():
                        if str(tokens[1]) in key:
                            flag = key
                    if flag:
                        print(objects[flag])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line=""):
        """prints all string representation of all instances"""
        objects = storage.all()
        list_objects = list()
        if line == "":
            for value in objects.values():
                list_objects.append(str(value))
            print(list_objects)
        elif line in self.classe.keys():
            for key, value in objects.items():
                if line in key:
                    list_objects.append(str(value))
            print(list_objects)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] in self.classe.keys():
                if len(tokens) == 1:
                    print("** instance id missing **")
                else:
                    objects = storage.all()
                    flag = None
                    for key in objects.keys():
                        if str(tokens[1]) in key:
                            flag = key
                    if flag:
                        del(objects[flag])
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """update an instance based on the class id"""
        tokens = shlex.split(line)
        integers = ['number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night']
        floats = ['latitude', 'longitude']
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1 and tokens[0] in self.classe.keys():
            print("** instance id missing **")
        elif tokens[0] not in self.classe.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            flag = 0
            for k in objects.keys():
                if str(tokens[1]) in k:
                    if tokens[2] in integers:
                        tokens[3] = int(tokens[3])
                    elif tokens[2] in floats:
                        tokens[3] = float(tokens[3])
                    setattr(objects[k], tokens[2], tokens[3])
                    objects[k].save()
                    flag = 1
            if flag == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()