#!/sur/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path  = "file.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        # converting python object into dictionary
        # writing to json
        with open(self.__file_path, mode="w") as f:
            tmp_storage = {}
            for k, v in self.__objects.items():
                tmp_storage[k] = v.to_dict()
            json.dump(self.__objects, f)
    
    def reload(self):
        classes = {
            "BaseModel":BaseModel
        }
        try:
             with open(self.__file_path, mode="r") as f:
                jo = json.load(f)
                for k in jo:
                    self.__objects[k] = classes[jo[k]["__class__"]](**jo[k])

        except FileNotFoundError:
            pass
