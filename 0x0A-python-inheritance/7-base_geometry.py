#!/usr/bin/python3
"""The python script defines a class BaseGeometry"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """
    def area(self):
        """The Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates value.

        Args:
            name (str): The name of the object.
            value (int): The value of the property.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
