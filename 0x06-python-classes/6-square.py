#!/usr/bin/python3
"""Square"""


class Square:
    """Instanciate square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square
        Args:
            size: length
            position: coordinates
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Props
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Props
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position of quare
        Args: value
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get area of Square
        Returns: Size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns coordinates"""
        cord = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            cord += "\n"
        for x in range(self.size):
            for y in range(self.position[0]):
                cord += " "
            for z in range(self.size):
                cord += "#"
            cord += "\n"
        return cord

    def my_print(self):
        """print the square"""
        print(self.pos_print(), end='')
