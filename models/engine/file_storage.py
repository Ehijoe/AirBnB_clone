#!/sur/bin/python3

""" module imported"""
import json, os, datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

class FileStorage:
    """ FileStoragte class definition """
    __file_path  = "file.json"
    __objects = {}


    def all(self):
        """ retrun the dictionary object """
        return self.__objects

    def new(self, obj):
        """ nsets in __object the obj with key """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        """ save methods """
        # converting python object into dictionary
        # writing to json
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            tmp_storage = {}
            for k, v in self.__objects.items():
                tmp_storage[k] = v.to_dict()
            json.dump(self.__objects, file)

    def reload(self):
        """ reload method """
        classes = {
            "BaseModel":BaseModel,
            "User": User,
            "State": State,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_data = json.load(file)
                for k in json_data:
                    self.__objects[k] = classes[json_data[k]["__class__"]](**json_data[k])

        except FileNotFoundError:
            pass

    def attributes(self):
        """returns valid attributes and their types for classname"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str 
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": str,
                "number_bathrooms": str,
                "max_quest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes
