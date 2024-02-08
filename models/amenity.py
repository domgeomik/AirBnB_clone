#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module class: Amenitymy
"""


class Amenitymy(BaseModel):
    """definition for class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
