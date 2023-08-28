#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Arguments:
        value (int): The integer to print.

    Return values:
        Returns False if a TypeError or ValueError occurs 
        Otherwise returns True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
