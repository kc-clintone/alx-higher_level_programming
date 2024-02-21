#!/usr/bin/python3
"""This module checks if object is an instance of a class or not"""
def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that is inherited
    from the specified class; else returns False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
