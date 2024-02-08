#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class Usermy(BaseModel):
    '''base model class'''

    email = ""
    password = ""
    last_name = ""
    first_name = ""
