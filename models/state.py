#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module class: Statemy
"""


class Statemy(BaseModel):
    """definition for class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
