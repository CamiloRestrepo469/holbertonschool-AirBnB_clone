#!/usr/bin/python3
"""Create a Class HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit the console.
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
