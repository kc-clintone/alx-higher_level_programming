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

    @property
    def size(self):
        """Well, this function gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Now, this function calculates the area of the square,
        if I'm not wrong.
        Returns: The area, kind of...
        """
        return (self.__size ** 2)
