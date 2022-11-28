#!/urs/bin/python3
""" modules imported """

from json import dump, load, dumps
from os.path import exists
from models import base_model
from models import city
from models import state
from models import review
from models import amenity
from models import place
from models import user

list_of_classes =["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

class FileStorage:
    """File Storage class definition"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictinary"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in  __objects the object with key
         <class name>.id
        """
        class_name = obj.__class__.__name__
        id = obj.id
        class_id = class_name + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """serializes __obejects  to the json file"""
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dump(dict_to_json, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dict_obj = {}
        FileStorage.__objects = {}
        if exists(FileStorage.__file_path):
            for key, value in dict_obj.items():
                class_name = key.split(".")[0]
                if class_name in list_of_classes:
                    FileStorage.__objects[key] = eval(class_name)(**value)
                else:
                    pass
