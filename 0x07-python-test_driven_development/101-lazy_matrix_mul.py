#!/usr/bin/python3.5
"""
Multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        Product of the two matrices
    """

    return (np.matmul(m_a, m_b))
