#!/usr/bin/python3
"""Let's engineer a class that deals with rectangles"""
class Rectangle:
    """Well now it does something"""
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def area(self):
        return (self.__height * self.__width)
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
    def __str__(self) -> str:
        if self.__height == 0 or self.__width == 0:
            return ("")
        rect = ""
        for c in range(self.__height):
            for r in range(self.__width):
                rect += "#"
            if c < self.__height - 1:
                rect += "\n"
        return (rect)
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__height, self.__width)
