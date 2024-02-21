#!/usr/bin/python3
"""This module contains a JSON file-writing function"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object/content to a UTF-8 text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
