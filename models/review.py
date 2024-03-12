#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class review model.
    """

    place_id = ""
    user_id = ""
    text = ""
