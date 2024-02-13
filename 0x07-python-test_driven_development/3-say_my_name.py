#!/usr/bin/python3
"""
This module has a function that prints your name (or simply a name)
"""
def say_my_name(first_name, last_name=""):
    # First, check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name to std
    print(f"My name is {first_name} {last_name}")

