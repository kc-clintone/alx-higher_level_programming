#!/usr/bin/python3
"""Docstring module"""
import math


class MagicClass:
    """Let's create magic"""

    def __init__(self, radius=0):
        """Docstring recreation"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Cont..."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """The end"""
        return 2 * math.pi * self.__radius
