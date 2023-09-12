#!/usr/bin/python3
"""The python script defines the Function add_attribute"""


def add_attribute(object, attr_name, value):
    """This function adds a new attribute to an object if it's possible.

    Args:
        object (__main__.MyClass): The name of the object.
        attr_name ('str): The name of the attribute.
        value (str): The value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
