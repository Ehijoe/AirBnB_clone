#!/usr/bin/python3
""" datetime, uuid modules """

from datetime import datetime
import uuid

# date format variable
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel definition"""

    def __init__(self):
        self.id = uuid.uuid4
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string formatter"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ " udpate updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """" to_dic method definition"""
        dic = {}

        for key, item in self.__dict__.items():
            if key in ["craeted_at", "updated_at"]:
                dic[key] = item
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
