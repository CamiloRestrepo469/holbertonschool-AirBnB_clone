#!/usr/bin/python3
"""Create a Class HBNBCommand"""

import cmd
import json
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.
    """

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console with EOF (Ctrl+D).
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Display help message for quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help message for EOF command.
        """
        print("Exit the console with EOF (Ctrl+D).")

    def help_help(self):
        """
        Display help message for help command.
        """
        print("Display help information.")


    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        instance = storage.classes[class_name]()
        instance.save()
        print(instance.id)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
