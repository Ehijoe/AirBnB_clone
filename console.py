#!/usr/bin/python3
""" Console """
import cmd
import shlex
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models import storage

classes_dict = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Place': Place,
    'Review': Review,
    'City': City,
    'Amenity': Amenity,
}

class HBNBCommand(cmd.Cmd):
    """ hbn command interpreter """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """ end the file """
        return True

    def do_quit(self, args):
        """ quite the program """
        return True

    def emptyline(self):
        """ Don't excecute notyhing """
        pass

    def do_create(self, args):
        """ Create a new instance """
        if not (args):
            print("** class name missing **")
        elif args not in classes_dict:
            print("** class don't exist **")
        else:
            instance = eval(args)()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints the string representation of and instance """
        if not (args):
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes_dict:
                print("** class doesn't exits **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value.id:
                        print(value)
                        return
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes the instance that matched the class id and name """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] not in classes_dict:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances """
        split_args = shlex.split(args)
        n_list = []
        dict_json = storage.all()
        if args:
            try:
                for key in dict_json:
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for key in storage.all():
                n_list.append(str(storage.all()))
            print(n_list)

    def do_update(self, args):
        """ Update an instance based of the class name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes_dict:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
