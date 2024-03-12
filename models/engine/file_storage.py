#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review


class FileStorage:
    """
    i will use this class to handle all serialization.
    and desiarilization.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the __objects dictionary.
        that contains all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This method adds a new object to the __objects.
        dictionary.
        """
        obname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obname, obj.id)] = obj

    def save(self):
        """
        This method serializes all objects in.
        __objects to JSON file.
        """
        mydict = FileStorage.__objects
        myobjdict = {obj: mydict[obj].to_dict() for obj in mydict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(myobjdict, file)

    def reload(self):
        """
        This method deserializes and also reloads.
        from json to __objects.
        """
        try:
            with open(FileStorage.__file_path) as file:
                myobjdict = json.load(file)
                for obj in myobjdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
