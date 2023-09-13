#!/usr/bin/python3
"""A module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """This function returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The json object to be converted to Python object.

    Returns:
        type: Returns a Python object.
    """
    """
    print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    print("type my_str--> {}".format(type(my_str)))
    """
    return json.loads(my_str)
