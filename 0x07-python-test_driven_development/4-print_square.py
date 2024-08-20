#!/usr/bin/python3
"""
This moduled contains a function that prints the # character
"""


def print_square(size):
    """
    This function prints a shape using the # charachter
    Args:
        Size of the sqaure
    Return:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
