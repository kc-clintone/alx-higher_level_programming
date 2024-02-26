#!/usr/bin/python3
"""Now this is a module...more later"""


class Square:
    """We add stuff...to the class"""
    def __init__(self, size=0):
        """Let's see what we've added
        args:
            size: size of the square
        raises:
            TypeError: if size != integer
            ValueError: if size < zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
