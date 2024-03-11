#!/usr/bi/python3
import json
from models.base_model import BaseModel

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
        return self.__objects

    def new(self, obj):
        """
        This method adds a new object to the __objects.
        dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        This method serializes all objects in.
        __objects to JSON file.
        """
        ser_objects = {}
        for key, obj in self.__objects.items():
            ser_objects[key] = obj.to_dict()


        with open(self.__file_path, w) as file:
            json.dump(ser_objects, file)


    def reload(self):
        """
        This method deserializes and also reloads.
        from json to __objects.
        """
        try:
            with open(self.__file_path, r) as file:
                loading_objects = json.load(file)

            for key, obj_dict in loading_objects.items():
            class_name, obj_id = key.split('.')
            class_ref = eval(class_name)
            obj = class_ref(**obj_dict)
            self.__objects[key] = obj
        except FileNotFoundError:
            pass

