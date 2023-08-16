#!/usr/bin/python3
'''returns a list with all values multiplied by a number'''
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
