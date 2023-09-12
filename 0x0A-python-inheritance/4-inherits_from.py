#!/usr/bin/python3
"""This python script defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """This function returns True if the object is an 
    instance of a class that inherited,
    (directly or indirectly) from the specified class, else it returns False.

    Args:
        obj (a_class): The object to check type.
        a_class (type): type of type to check.

    Returns:
       A boolean: True or False..
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
