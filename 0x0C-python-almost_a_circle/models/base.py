#!/usr/bin/python3
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

