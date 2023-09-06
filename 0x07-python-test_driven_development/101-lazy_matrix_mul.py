#!/usr/bin/python3
# 101-lazy_matrix_mul.py

import numpy as np

"""This python script defines 
a matrix multiplication function using NumPy."""

def lazy_matrix_mul(m_a, m_b):
    """This function returns the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))

