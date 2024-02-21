#!/usr/bin/python3
"""This module contains a JSON-to-object conversion function"""

import json

def from_json_string(my_str):
    """This function returns the Python object version of a JSON string"""
    return json.loads(my_str)
