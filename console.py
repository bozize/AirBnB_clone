#!/usr/bin/python3
"""
Module console
"""
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


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    This class defines the hbnb command interpreter.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    def emptyline(self):
        """
        This method does nothing when it encounters an empty line.
        """
        pass

    def default(self, arg):
        """
        This method handles the default behavior.
        when the input is invalid.
        """
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        like = re.search(r"\.", arg)
        if like is not None:
            argm = [arg[:like.span()[0]], arg[like.span()[1]:]]
            like = re.search(r"\((.*?)\)", argm[1])
            if like is not None:
                command = [argm[1][:like.span()[0]], like.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argm[0], command[1])
                    return argdict[command[0]](call)
            print("*** Unknown syntax: {}".format(arg))
            return False

    def do_quit(self, arg):
        """
        This the quit command to exit.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal for exit program.
        """
        print("")
        return True

    def do_show(self, arg):
        """
        This command displays the string represenation.
        of a class instance of a given id.
        """
        argm = parse(arg)
        myobjdict = storage.all()
        if len(argm) == 0:
            print("** missing class name **")
        elif argm[0] not in HBNBCommand.__classes:
            print("** class doesnt exist **")
        elif len(argm) == 1:
            print("** missing instance id **")
        elif "{}.{}".format(argm[0], argm[1]) not in myobjdict:
            print("** No instance found **")
        else:
            print(myobjdict["{}.{}".format(argm[0], argm[1])])

    def do_create(self, arg):
        """
        This command creates a new class instance.
        prints its id.
        """
        argm = parse(arg)
        if len(argm) == 0:
            print("** missing class name **")
        elif argm[0] not in HBNBCommand.__classes:
            print("** class doesnt exist **")
        else:
            new_instance = eval(argm[0])()
            print(new_instance.id)
            storage.save()

    def do_destroy(self, arg):
        """
        command deletes class instance given id.
        """
        argm = parse(arg)
        myobjdict = storage.all()
        if len(argm) == 0:
            print("** missing class name **")
        elif argm[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(argm) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argm[0], argm[1]) not in myobjdict.keys():
            print("** found no instance **")
        else:
            del myobjdict["{}.{}".format(argm[0], argm[1])]
            storage.save()

    def do_all(self, arg):
        """
        this display the string representations of all instances.
        given class.
        if no class given it displays all objects.
        """
        argm = parse(arg)
        if len(argm) > 0 and argm[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        else:
            objm = []
            for obj in storage.all().values():
                if len(argm) > 0 and argm[0] == obj.__class__.__name__:
                    objm.append(str(obj))
                elif len(argm) == 0:
                    objm.append(str(obj))
            print(objm)

    def do_count(self, arg):
        """
        Counts the number of instances of given class
        """
        argm = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argm[0] == obj.__class__.name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        This updates instance class of a given
        """
        argm = parse(arg)
        myobjdict = storage.all()

        if len(argm) == 0:
            print("** missing class name **")
            return False
        if argm[0] not in HBNBCommand._classes:
            print("** class does not exist **")
            return False
        if len(argm) == 1:
            print("** indtance id missing **")
            return False
        if "{}.{}".format(argm[0], argm[1]) not in myobjdict.keys():
            print("** found no instance **")
            return False
        if len(argm) == 2:
            print("** missing attribute name **")
            return False
        if len(argm) == 3:
            print("** value misiing **")
            return False

        obj = myobjdict["{}.{}".format(argm[0], argm[1])]
        if argm[2] in ["id", "created_at", "updated_at"]:
            print("** cannot update **")
            return False

        if argm[2] not in obj.__class__.__dict.keys():
            print("** attribute doesnt exist ** ")
            return False

        attr_type = type(obj.__class__.__dict__[argm[2]])
        setattr(obj, argm[2], attr_type(argm[3]))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
