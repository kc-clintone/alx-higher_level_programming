#!/usr/bin/python3
"""This module defines a Student main class"""


class Student:
    """This represent a student class"""
    def __init__(self, first_name, last_name, age):
        """Initializing a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Refrences a dictionary representation of the Student object"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student object/class"""
        for k, v in json.items():
            setattr(self, k, v)
