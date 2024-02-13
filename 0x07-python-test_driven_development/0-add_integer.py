#!/usr/bin/python3
"""
This function/module has one function that adds two integers.
"""

def add_integer(a, b=98):
    """Returns sum of two integers/floats as integers

    Arguments:
        a: The first argument
        b: The second argument

    Returns:
        Sum of the two arguments passed to the funtion.

    Raises the exception:
        TypeError: If neither of the arguments aint an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
