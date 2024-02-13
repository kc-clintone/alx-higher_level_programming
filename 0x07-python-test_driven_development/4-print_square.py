#!/usr/bin/python3
"""
This moduled contains a function that prints the # character
"""
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        print("#" * size)
