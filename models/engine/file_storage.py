#!/usr/bin/python3
"""
Module that serialize and deserialize JSON file
"""
import json
from models.base_model import BaseModel


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
        """deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
