#!/usr/bin/python3
def matrix_divided(matrix, div):
    # First, check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Then, check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Now, check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Next, check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Lastly, perform the matrix division and round to 2 decimal places
    final_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return final_matrix
