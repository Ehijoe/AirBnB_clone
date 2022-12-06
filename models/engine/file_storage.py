#!/sur/bin/python3

from json import dump, load
from os.path import exists

list_of_classes = ["BaseModel", "User", "State", "City",
                   "Place", "Amenity", "Review"]

class FileStorage:
    """File Storage class definition."""

    __file_path = "file.json"
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
            dump(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
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