#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This function prints x elements of a list
    """
    return_value = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            return_value += 1
        except IndexError:
            break
    print("")
    return (return_value)
