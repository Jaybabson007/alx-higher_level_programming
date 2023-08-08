#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, c):
    """This function should match the bytecode provided in the question"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
