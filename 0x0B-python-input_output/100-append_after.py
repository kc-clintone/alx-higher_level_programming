#!/usr/bin/python3
"""This module defines a text/file insertion function"""

def append_after(filename="", search_string="", new_string=""):
    """This function inserts text after each line containing a given string in a file"""
    the_txt = ""
    with open(filename) as r:
        for i in r:
            the_txt += i
            if search_string in i:
                the_txt += new_string
    with open(filename, "w") as w:
        w.write(the_txt)
