#!/usr/bin/python3
""" Module for Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review inherited from BaseModel """

    place_id = ""
    user_ide = ""
    text = ""
