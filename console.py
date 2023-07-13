#!/usr/bin/python3
import cmd

"""create a class HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when End-of-File (EOF) is reached"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Quit the program"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Quit the program when"""
        print("exit with an empty line")

    def help_help(self):
        """Quit the program"""
        print("help with an empty line")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
