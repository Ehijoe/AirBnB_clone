#!/usr/bin/python3
"""Base Model."""

from datetime import datetime
import uuid
from models import storage

# date format variable
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel definition."""

    def __init__(self, *args, **kwargs):
        """Initialize the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, DATETIME_FORMAT)

                if key not in ["__class__"]:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return the string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Set the updated_at attribute."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return the the dictionary representation."""
        dic = {}

        for key, item in self.__dict__.items():
            dic[key] = item
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
