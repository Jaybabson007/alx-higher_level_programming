#!/usr/bin/python3
"""A module defining the class Student"""


class Student:
    """
   A  Class that defines properties of student.

    Attributes:
        first_name (str): The first name of student.
        last_name (int): The last name of student.
        age (int): The age of student.
    """
    def __init__(self, first_name, last_name, age):
        """This function creates new instances of Student.

        Args:
            first_name (str): The first name of student.
            last_name (int): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function retrieves a dictionary representation of a Student instance.

        Returns:
            dict: returns a  dictionary representation.
        """
        return self.__dict__
