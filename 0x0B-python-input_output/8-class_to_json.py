#!/usr/bin/python3
"""A module containing the function class_to_json"""


def class_to_json(obj):
    """This function returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean) for JSON serialization,
    of an object.

    Args:
        obj (MyClass): An object.

    Returns:
        dict: A dictionary.
    """
    # print("type of obj --> {}".format(type(obj)))
    return obj.__dict__
