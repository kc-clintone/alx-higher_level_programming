#!/usr/bin/python3

"""This is a base class"""

import json

class Base:
    """
    Base class for managing id attribute in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int): If provided, assign it to the public instance attribute id.
                      If not provided, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Here, we convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): a List of dictionaries.

        Returns:
            str: a JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writing the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): a List of instances inheriting from Base.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Now we convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): a JSON string representing a list of dictionaries.

        Returns:
            list: a List represented by the JSON string.
        """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)
