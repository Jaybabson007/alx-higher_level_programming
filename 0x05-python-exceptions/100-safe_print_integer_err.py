#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """This function Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Arguments:
        value (int): The integer to print.

    Return value:
       Returns False If a TypeError or ValueError occurs,
         Otherwise it returns True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
