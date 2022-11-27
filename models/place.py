#!/usr/bin/python3
""" base_model import """

from models.base_model import BaseModel

class Place(BaseModel):
    """ Place class definition """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = ""
    number_bathroom = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    