#!/usr/bin/python3
"""Console interface for AirBnB app."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City

classes = {
    'Basemodel': BaseModel,
    'User': User,
    'State': State,
    'Place': Place,
    'Review': Review,
    'City': City,
    'Amenity': Amenity,
}

storage.reload()


class HBNBCommand(cmd.Cmd):
    """Defines the Interpreter class HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command and exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program in non-interactive mode."""
        return True

    def do_create(self, args):
        """Create instance of a model."""
        args = shlex.split(args)
        if not (args):
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            temp = eval(args[0])()
            storage.new(temp)
            temp.save()
            print(temp.id)
        else:
            print("** Too many arguments for create **")

    def do_show(self, args):
        """Print the string representation of and instance."""
        args = shlex.split(args)
        if args[0] not in classes:
            print("** class doesn't exits **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            print(str(storage.search(f"{args[0]}.{args[1]}")))

    def do_destroy(self, args):
        """Delete the instance that matched the class id and name."""
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
            print("** no instance found **")

    def do_all(self, args):
        """Print all string representation of all instances."""
        args = shlex.split(args)
        n_list = []
        if args:
            try:
                for key in storage.all():
                    if args[0] == key.split('.')[0]:
                        n_list.append(str(storage.all()[key]))
                print(n_list)
            except ModuleNotFoundError:
                print("** class doesn't exist **")
        else:
            for key in storage.all():
                n_list.append(str(storage.all()))
            print(n_list)

    def do_update(self, args):
        """Update an instance based of the class name and id."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance doesn't exist **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
