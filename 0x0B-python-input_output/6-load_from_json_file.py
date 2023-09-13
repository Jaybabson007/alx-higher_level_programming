#!/usr/bin/python3
"""A module containing the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """This function creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file.

    Returns:
        object- returns an object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
