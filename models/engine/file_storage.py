#!/urs/bin/python3
""" modules imported """


class FileStorange:
    """File Storage class definition"""

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """returns a dictinary"""
        return self.__objects

    def new(self):
        """
        sets in  __objects the object with key
         <class name>.id
        """
        pass

    def save(self):
        """serializes __obejects  to the json file"""
        pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        pass
    
