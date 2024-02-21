#!/usr/bin/python3
"""This module contains a JSON file-reading function"""


import json


def load_from_json_file(filename):
    """This function creates a Python object from reading a given JSON file"""
    with open(filename) as f:
        return json.load(f)
