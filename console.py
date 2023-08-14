#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

CLASS_MAPPING = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
        }

ARGUMENT_PATTERN = re.compile(r"([\w]+)(?:\((.*?)\))?")

def parse_arguments(arg):
    match = ARGUMENT_PATTERN.match(arg)
    if match:
        command = match.group(1)
        args = match.group(2)
        if args:
            args_list = [a.strip() for a in args.split(",")]
            return command, args_list
        return command, []
    return None, []

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def default(self, arg):
        command, args = parse_arguments(arg)
        if command == "quit":
            return True
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, arg):
        command, args = parse_arguments(arg)
        if not command:
            print("** class name missing **")
        elif command not in CLASS_MAPPING:
            print("** class doesn't exist **")
        else:
            instance = CLASS_MAPPING[command]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        command, args = parse_arguments(arg)
        if not command:
            print("** class name missing **")
        elif command not in CLASS_MAPPING:
            print("** class doesn't exist **")
        elif len(args) == 0:
            print("** instance id missing **")
        else:
            instance_id = "{}.{}".format(command, args[0])
            objects = storage.all()
            if instance_id in objects:
                print(objects[instance_id])
            else:
                print("** no instance found **")

    # Define other command methods (do_destroy, do_all, do_count, do_update)

if __name__ == "__main__":
    HBNBCommand().cmdloop()

