#!/usr/bin/python3
"""File storage module."""
from json import dump, load
from os.path import exists

list_of_classes = ["BaseModel", "User", "State", "City",
                   "Place", "Amenity", "Review"]


class FileStorage:
    """File Storage class definition."""

    __file_path = "file.json"
    __objects = {}

    def search(self, id):
        """Search for an object in the storage."""
        return self.__objects.get(id)

    def all(self):
        """Return the dictionary object."""
        return self.__objects

    def new(self, obj):
        """Set in __object the obj with key."""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save objects to json file."""
        # converting python object into dictionary
        # writing to json
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            tmp_storage = {}
            for k, v in self.__objects.items():
                tmp_storage[k] = v.to_dict()
            dump(tmp_storage, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City

        dict_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path) as json_file:
                dict_obj = load(json_file)
            for key, value in dict_obj.items():
                class_name = key.split(".")[0]
                if class_name in list_of_classes:
                    FileStorage.__objects[key] = eval(class_name)(**value)
                else:
                    pass
