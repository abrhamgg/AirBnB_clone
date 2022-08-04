#!/usr/bin/env python3
"""
Command intrepretor
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """command intrepretor"""
    def __init__(self):
        """initializing the interpreter"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, args):
        """method to quit the interpreter"""
        sys.exit(1)

    def do_EOF(self, args):
        """end of file"""
        return True


if __name__ == "__main__":
    CLI = HBNBCommand()
    CLI.cmdloop()
