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


def print_error(message):
    """
    Helper function to print error messages.
    """
    print("Error: {}".format(message))

def show_command(arguments):
    """
    Implementation of the 'show' command.
    """
    if len(arguments) == 0:
        print_error("class name missing")
        return
    class_name = arguments[0]
    if class_name not in class_dict:
        print_error("class doesn't exist")
        return
    if len(arguments) == 1:
        print_error("instance id missing")
        return
    instance_id = arguments[1]
    try:
        instance = class_dict[class_name].get(instance_id)
        print(instance)
    except KeyError:
        print_error("no instance found")



    def do_show(self, arg):
        """
        Display the string representation of an instance.
        Usage: show <class_name> <id>
        """
        arguments = arg.split()
        show_command(arguments)

    def help_show(self):
        """
        Display help message for show command.
        """
        print("Display the string representation of an instance.")
        print("Usage: show <class_name> <id>")

if __name__ == '__main__':
    HBNBCommand().cmdloop()