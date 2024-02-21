#!/usr/bin/python3
"""Defines Rectangle, inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines object rectangle from BaseGeometry"""

    def __init__(self, width, height):
        """Intializing new rectangle object"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    def area(self):
        """Returns area of rectangle"""

        return self.__width * self.__height
    def __str__(self):
        """Returns the print() and str() repr methods of the Rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
