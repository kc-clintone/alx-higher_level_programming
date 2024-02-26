#!/usr/bin/python3
"""This here is a quare module"""


class Square:
    """Define the Square"""
    def __str__(self):
        """Print"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the square
        Args:
            size: Side
            position: Coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """props
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square
        Args:
            value: The size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """props
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: Position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: Position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Area
        Returns:
            size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """Print"""
        position_ = ""
        if not self.size:
            return "\n"
        for x in range(self.position[1]):
            position_ += "\n"
        for x in range(self.size):
            for y in range(self.position[0]):
                position_ += " "
            for z in range(self.size):
                position_ += "#"
            position_ += "\n"
        return position_

    def _print(self):
        """print square"""
        print(self.print_position(), end="")
