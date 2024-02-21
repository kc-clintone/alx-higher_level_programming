#!/usr/bin/python3
"""Inherits from list class"""


class MyList(list):
    """Inherits from the List class and prints a sorted list"""
    def print_sorted(self):
        print(sorted(self))
