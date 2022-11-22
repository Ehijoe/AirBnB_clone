#!/usr/bin/python3
""" datetime, uuid modules """

from datetime import datatime
import uuid

# variable to store datetime format
datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """ BaseModel Class definition """

    def __init__(self):
        self.id = uuid.uuid4
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """ format a string """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    def save(self):
        """ update the public instance updated_at with current datetime """
        self.update_at = datetime.now()

    def to_dict(self):
        """ return dictionary containting """

        dictinary = {}
        for key. item in self.__dict__.items():
            for key in ["created_at", "updated_at"]:
                dictinary[key] = item 
            
        dictinary["__class__"] = self.__class__.__name__
        dictinary["created_at"] = self.created_at.isoformat()
        dictinary["updated_at"] = self.updated_at.isoformat()

        return dictinary
