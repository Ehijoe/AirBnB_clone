#!/usr/bin/python3
""" base_model import """

from models.base_model import BaseModel

class User(BaseModel):
    """ User class defination """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
