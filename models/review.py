#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
Module class: Reviewmy
"""


class Reviewmy(BaseModel):
    """definition for class Review"""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
