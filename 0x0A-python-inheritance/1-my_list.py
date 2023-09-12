#!/usr/bin/python3
"""The python script defines a class called MyList that inherits  list"""


class MyList(list):
    """A Class that inherits  list.

    Args:
        list (list): the list to sort in ascending order.
    """
    def print_sorted(self):
        """This prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
