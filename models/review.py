#!/usr/bin/python3
"""base model import."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition."""

    place_id = ""
    user_id = ""
    text = ""
