#!/usr/bin/python3
"""Inheris from baseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define rectangle from the class BaseGeometry"""
    def __init__(self, width, height):
        """Intializing a new Rectangle object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
