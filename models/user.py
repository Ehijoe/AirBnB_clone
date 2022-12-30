#!/usr/bin/python3
"""Model for Users."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class definition."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
