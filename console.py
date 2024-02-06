#!/usr/bin/python3

import cmd
import string
import sys


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_hello(self, arg):
        """ The hello mode """
        print("Hello,", arg)

    def emptyline(self):
        print("Empty line! Type 'hello' followed by a name.")

    def do_quit(self, arg):
        """ The method quits from the interactive mode"""
        return True

    def default(self, line):
        """ the default mode """
        print(f"This commnad is not in the console {line}")

    def do_EOF(self, arg):
        """ Exits out of the EOF command line"""
        return True


if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop("Welcome to Chris's Console")
