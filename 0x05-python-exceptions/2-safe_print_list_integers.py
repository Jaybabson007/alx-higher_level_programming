#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """This function Prints the first x elements of a list that are integers.

    Arguments:
        my_list (list): The list to print the elements from.
        x (int): The number of elements of my_list to be  printed.

    Return value:
        The number of elements printed.
    """
    return_value = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            return_value += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (return_value)

