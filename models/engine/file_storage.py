#!/usr/bin/python3
"""
Module that serialize and deserialize JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    FileStorage serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        c_id = obj.id
        class_id = class_name + "." + c_id
        self.__objects[class_id] = obj

    def save(self):
        """method that serialize python object to JSON file"""
        with open(self.__file_path, "w") as f:
            a_dict = {}
            for k, v in self.__objects.items():
                a_dict[k] = v.to_dict()
            json.dump(a_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
