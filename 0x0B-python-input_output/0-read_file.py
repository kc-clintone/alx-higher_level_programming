#!/usr/bin/python3
"""This module has a funtion for text/file reading capability"""

def read_file(filename=""):
    """This function prints contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
