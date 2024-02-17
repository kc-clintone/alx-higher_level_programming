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

    def update(self, *args, **kwargs):
        """
        Assigning arguments to attributes based on their type, more args.

        Args:
            *args: No-keyword arguments in the order (id, size, x, y).
            **kwargs: Key-worded arguments representing attribute assignments.
        """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Now, the dictionary for the square. Returns the dictionary
           representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Override the __str__ method."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

