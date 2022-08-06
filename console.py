#!/usr/bin/env python3
"""
Command intrepretor
"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models import storage

arguments = ['BaseModel', 'User']


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

    def do_create(self, args):
        """Creates a new instance of BaseMOodel and saves it to JSONFILE
        and prints the id
        if class name is missing it prints *** class name missing**
        if class name doesnt exist print *** class doesnt exists ***
        """
        if not args:
            print("** class name missing **")
        if args not in arguments:
            print("** class doesn't exist **")
        else:
            b1 = BaseModel()
            b1.save()
            print(b1.id)

    def do_show(self, args):
        """print the string representation of
        instance based on class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in arguments:
                print("** class doesn't exist **")
            else:
                key = args[0] + '.' + args[1]
                for k, v in storage.all().items():
                    if k == key:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on class name
        and id (save changes to JSON file)
        """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in arguments:
                print("** class doesn't exist **")
            else:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """prints string representation of all
        instance based or not on the class name"""
        arg_list = args.split()
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in arguments:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, args):
        """Updates an instance based on class name and id
        by adding or updating attribute
        """
        args = args.split()
        if len(args) == 0:
            print("*** class name missing ***")
            return False
        if args[0] in arguments:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key],
                                    args[2], args[3].strip('"'))
                            storage.all()[key].save()
                        else:
                            print("*** value missing ***")
                    else:
                        print("*** attribute name missing ***")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
