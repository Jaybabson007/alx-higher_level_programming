#!/usr/bin/python3
"""The python script returns a function lookup()"""


def lookup(obj):
    """This function returns the list of available attributes and methods
    of an object

    Args:
        obj (class): the object

    Returns:
        list: The list of available attributes and methods of an object
    """
    return dir(obj)
