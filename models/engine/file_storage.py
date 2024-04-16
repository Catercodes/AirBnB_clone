#!/usr/bin/python3
""" This module contains  Filestorage"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """The Private class attribute"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "return  the  dict of the class attr '__object' """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in the __object with the key to obj"""
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' This method save the convert the __object into
        a json string'''
        _dict = {}
        with open(FileStorage.__file_path, 'w',) as json_file:
            for key, value in FileStorage.__objects.items():
                _dict[key] = value.to_dict()
                json.dump(_dict, json_file)

    def reload(self):
        """
        deserializes instances got from json file
        """
        try:
            with open(FileStorage.__file_path, 'r') as file_json:
                # _dict = json.load(file_json)
                # _dict = json.loads(file_json.read())
                data = json.load(file_json)
                from models.base_model import BaseModel
                for key, value in data.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
