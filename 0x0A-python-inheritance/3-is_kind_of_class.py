#!/usr/bin/python3
"""Checks if a class is inherited or not"""

def is_kind_of_class(obj, a_class):
    """Returns true if a class is inherited or the class that is inherited
    from
    """
    return (isinstance(obj, a_class))
