#!/usr/bin/python3
"""Console interface for the AirBnB clone."""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command line app."""

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Exit the program."""
        sys.exit()

    def do_quit(self, args):
        """Exit the program."""
        sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
