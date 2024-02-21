#!/usr/bin/python3
"""This module contains a file-writing function"""

def write_file(filename="", text=""):
    """This function writes a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
