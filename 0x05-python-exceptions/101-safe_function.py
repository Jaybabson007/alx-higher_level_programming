#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """This function executes a function safely.

    Arguments:
        fct: function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs, nothing
        else it returns the result of the function call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
