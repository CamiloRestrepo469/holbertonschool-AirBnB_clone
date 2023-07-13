#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def quit(self, arg):
        """Quit command to exit the program"""
        return True

    def EOF(self, arg):
        """Exit the program when End-of-File (EOF) is reached"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        if self.emptyline is None:
            self.emptyline = '\n'
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    