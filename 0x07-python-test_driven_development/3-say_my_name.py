#!/usr/bin/python3
"""
This module has a function that prints your name (or simply a name)
"""


def say_my_name(first_name, last_name=""):
    """
    This dunction prints a first name and a last name
    Args:
        first_name: first name
        last_name: last name
    Returns:
        Nothing
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
