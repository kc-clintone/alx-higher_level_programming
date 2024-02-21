#!/usr/bin/python3
"""This module contains a Python class-to-JSON function"""


def class_to_json(obj):
    """This function returns a dictionary version of a simple data structure"""
    return obj.__dict__
