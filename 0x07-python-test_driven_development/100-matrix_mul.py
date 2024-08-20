#!/usr/bin/python3
"""
Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        Product of two matrices
    Raises:
        TypeError: if m_a or m_b are not lists
        TypeError: if m_a or m_b are not a list of lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b do not have integers or floats
        TypeError: if m_a or m_b do not have the same size
        ValueError: if m_a and m_b can't be multiplied
    """
    rows, cols = validateMat(m_a, m_b)
    m_b_T = transpose(m_b)

    linear_vector = []
    for i in m_a:
        for j in m_b_T:
            linear_vector.append(dot_product(i, j))

    return linear_to_shape(linear_v, cols, rows)


def dot_product(v1, v2):
    """
    Function for multiplication
    Args:
        v1: vector1
        v2: vector2

    Returns:
        Result
    """
    total = 0
    for i, j in zip(v1, v2):
        total += (i * j)

    return total


def validateMat(mat_A, mat_B):
    """
    Function to validate matrices
    Args:
        mat_A: matrix A
        mat_B: matrix B

    Returns:
        number of rows and number of cols
    """
    if not isinstance(mat_A, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(mat_A[0], list):
        raise TypeError("m_a must be a list of lists")
    else:
        for i in mat_A[1:]:
            if not isinstance(i, list):
                raise TypeError("m_a must be a list of lists")

    if not isinstance(mat_B, list):
        raise TypeError("m_b must be a list")
    elif not isinstance(mat_B[0], list):
        raise TypeError("m_b must be a list of lists")
    else:
        for i in mat_B[1:]:
            if not isinstance(i, list):
                raise TypeError("m_b must be a list of lists")

    try:
        if not mat_A or not mat_A[0]:
            raise ValueError("m_a can't be empty")
    except IndexError:
        raise ValueError("m_a can't be empty")

    try:
        if not mat_B or not mat_B[0]:
            raise ValueError("m_b can't be empty")
    except IndexError:
        raise ValueError("m_b can't be empty")

    for i in mat_A:
        for h in i:
            if not isinstance(h, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for i in mat_B:
        for h in i:
            if not isinstance(h, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for i in range(1, len(mat_A)):
        if len(mat_A[i]) != len(mat_A[i-1]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(1, len(mat_B)):
        if len(mat_B[i]) != len(mat_B[i-1]):
            raise TypeError("each row of m_b must be of the same size")

    cols = len(mat_A[0])

    rows = 0
    for i in mat_B:
        rows += 1

    if cols == rows:
        return (rows, cols)

    raise ValueError("m_a and m_b can't be multiplied")


def transpose(mtx):
    """
    Function to transpose a matrix
    Args:
        mat: Target matrix
    Returns:
        tranposed matrix
    """
    cols = len(mtx[0])
    rows = 1
    for i in mtx[1:]:
        rows += 1
        if len(i) != cols:
            return ValueError("m_a and m_b can't be multiplied")

    matT = [[0 for j in range(rows)] for i in range(cols)]

    for j in range(cols):
        for i in range(rows):
            matT[j][i] = mtx[i][j]

    return matT


def linear_to_shape(linear_vector, rows, cols):
    """
    Converts a vector to row*col matrix
    Args:
        linear_v: 1D vector
        rows: number of rows
        cols: number of columns
    Returns:
        rows*cols matrix
    """
    mtx = []
    vector = linear_vector.copy()
    for i in range(rows):
        tmp = []
        try:
            for j in range(cols):
                tmp.append(vector.pop(0))
            mtx.append(tmp)
        except IndexError:
            break

    return mtx
