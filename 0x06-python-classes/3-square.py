#!/usr/bin/python3
"""Still a continuation, just expanding the class"""


class Square:
    """You already know what this is"""
    def __init__(self, size=0):
        """Same descriptions as before
        args:
            size: size of sqaure
        raises:
            TypeError: if size != integer
            ValueError: if size < zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """
        Now, this function calculates the area of the square,
        if I'm not wrong.
        Returns: The area
        """
        return (self.__size ** 2)
