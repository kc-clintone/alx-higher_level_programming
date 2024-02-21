#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """This class invert int operators == and !="""
    def __eq__(self, value):
        """Overrides the == opeartor with the != behavior"""
        return self.real != value
    def __ne__(self, value):
        """Overrides the != operator with the == behavior"""
        return self.real == value
