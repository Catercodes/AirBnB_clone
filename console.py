#!/usr/bin/python3
"""The module contains my console"""
import cmd
import string
import sys


class MyCmd(cmd.Cmd):
    """ The cmd"""
    prompt = "(hbnb) "

    def do_hello(self, arg):
        """ The hello mode """
        print("Hello,", arg)

    def emptyline(self):
        """ This take care of Emptyline"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        """ the default mode """
        print(f"This commnad is not in the console {line}")

    def do_EOF(self, arg):
        """ Exits out of the EOF command line"""
        return True
    def do_create(self, line):
        if line == '':
            print("** class name missing **")
        elif line  !=  MyCmd.classes:
            print("** class doesn't exist **")
        else:
            storage.save()
            print(obj.id)


if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()
