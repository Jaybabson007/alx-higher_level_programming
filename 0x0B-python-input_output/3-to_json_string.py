#!/usr/bin/python3
"""A module containing the function to_json_string"""
import json


def to_json_string(my_obj):
    """This function Returns the JSON representation of an object(string).

    Args:
        my_obj (type): The object to examine.

    Returns:
        str: returns the JSON representation of object.
    """

    """ 
    print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    print("type my_obj--> {}".format(type(my_obj)))
    """

    # Serializing json
    return json.dumps(my_obj)
