#!/usr/bin/python3
"""Let's engineer a class that deals with rectangles"""


class Rectangle:
    """Well now it does something"""
    def __init__(self, width=0, height=0):
       """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """height setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """calculate height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
       self.__height = value

    @property
    def width(self):
        """widty setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """calculate width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
