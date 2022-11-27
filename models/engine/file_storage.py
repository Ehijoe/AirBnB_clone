#!/urs/bin/python3
""" modules imported """

from json import dump, load
from os.path import exists
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.user import User

list_of_classes = [BaseModel, User, State, City, Place, Amenity, Review]

class FileStorage:
    """File Storage class definition."""

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
        class_id = class_name + "." + obj.id
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
        if (exists(FileStorage.__file_path)):
            dict_obj = load(FileStorage.__file_path)
            for key, value in dict_obj.items():
                class_name = key.split(".")[0]
                if class_name in [cls.__name__ for cls in list_of_classes]:
                    FileStorage.__objects[key] = eval(class_name)(**value)
                else:
                    pass
