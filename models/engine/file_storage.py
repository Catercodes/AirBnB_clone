#!/usr/bin/python3
import json
import os
"""The python shebang"""


class FileStorage:
    """The Private class attribute"""
    __file_path = "file.json"
    __object = {}

    @classmethod
    def all(cls):
        "return  the  dict of the class attr '__object' """
        return cls.__object

    def new(self, obj):
        """ sets in the __object with the key to obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w',) as json_file:
            data = {key: value.__dict__ for key,
                value in FileStorage.__object.item()}
            json.dump(data, json_file)

#    def relaod(self):
#        if os.path.exists(FileStorage.__file_path):
#            with open(FileStorage.file_path, 'r') as json_file:
#                data = json.load(json_file)
#                for key, value in data.item():
#        
#
#        else:
#            except FileNotFoundError:
#               pass

#    @classmethod
    def reload(self):
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                    # Here, you would reconstruct your objects based on the data
                    # Assuming `value` contains the necessary information to reconstruct objects
                        pass  # Placeholder for object reconstruction
        except FileNotFoundError:
            pass

        
