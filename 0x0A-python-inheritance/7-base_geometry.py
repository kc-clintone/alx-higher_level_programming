#!/usr/bin/python3
"""This module defines the base geometry class"""


class BaseGeometry:
    """The base class"""

    def area(self):
        """An unimplemented class"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Checks and validates integer values"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
