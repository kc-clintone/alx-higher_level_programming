#!/usr/bin/python3
"""Still a continuation, just expanding the class"""


class Square:
    """You already know what this is"""
    def __init__(self, size=0):
        """Same descriptions as before
        args:
            size: size of sqaure
        raises:
            TypeError: if size != integer
            ValueError: if size < zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Well, this function gets the size of the square"""
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
        """Coordinates of the square...is it? """
        return self.__position

    @position.setter
    def position(self, value):
        """All conditions still hold, now let's set the position """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def print_position(self):
        """returns the vector position of the square"""
        _position = ""
        if self.size == 0:
            return "\n"
        for t in range(self.position[1]):
            _position += "\n"
        for t in range(self.size):
            for i in range(self.position[0]):
                _position += " "
            for j in range(self.size):
                _position += "#"
            _position += "\n"
        return _position

    def my_print(self):
        """I guess this fn uses the character # to print the square"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            print("#" * self.__size)
