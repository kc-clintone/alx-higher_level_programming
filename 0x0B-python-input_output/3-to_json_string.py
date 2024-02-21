#!/usr/bin/python3
"""This module contains a string-to-JSON convertion function"""


import json


def to_json_string(my_obj):
    """Thie function returns the JSON version of a string object"""
    return json.dumps(my_obj)
