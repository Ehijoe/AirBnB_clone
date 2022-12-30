#!/usr/bin/python3
"""Model for Users."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class definition."""

    def __init__(self, *args, **kwargs):
        """Initialize the User."""
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
