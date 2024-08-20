#!/usr/bin/python3
"""
Matrix division
"""


def matrix_divided(matrix, div):
    """
    Check if matrix is a list of lists of integers or floats
    """
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    final_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return final_matrix
