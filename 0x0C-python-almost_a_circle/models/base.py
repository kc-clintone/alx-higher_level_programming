#!/usr/bin/python3

"""This is a base class"""

import json
import csv
import turtle
import os

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

    @classmethod
    def create(cls, **dictionary):
        """
        Creating an instance with all of the attributes set using the update method.

        Args:
            **dictionary: a Double pointer to a dictionary containing attribute values.

        Returns:
            instance: an instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: a List of instances loaded from the file.
        """
        f_name = f"{cls.__name__}.json"
        try:
            with open(f_name, 'r') as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**obj) for obj in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writing the CSV representation of list_objs to a file.

        Args:
            list_objs (list): a List of instances inheriting from Base.
        """
        f_name = f"{cls.__name__}.csv"
        with open(f_name, 'w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a CSV file.

        Returns:
            list: a List of instances loaded from the file.
        """
        f_name = f"{cls.__name__}.csv"
        try:
            with open(f_name, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instances.append(cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])))
                    elif cls.__name__ == "Square":
                        instances.append(cls(int(row[0]), int(row[1]), int(row[2]), int(row[3])))
                return instances
        except FileNotFoundError:
            return []


    #Now we draw shapes
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Let's draw the rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): a List of Rectangle instances.
            list_squares (list): a List of Square instances.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Drawing Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
