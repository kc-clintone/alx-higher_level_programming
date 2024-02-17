#!/usr/bin/python3
"""The square module, it inherits the rectangle class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            size (int): Size of the square (width and height).
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): ID of the square.
        """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

