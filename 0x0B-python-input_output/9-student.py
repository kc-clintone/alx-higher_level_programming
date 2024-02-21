#!/usr/bin/python3
"""This module defines a Student main class"""


class Student:
    """This represent a student class"""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Refrences the dict representation of the Student"""
        return self.__dict__
