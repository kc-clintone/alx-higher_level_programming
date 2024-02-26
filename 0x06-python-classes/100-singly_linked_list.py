#!/usr/bin/python3
"""This module is a singly linked list...kinda"""


class Node:
    """"Let's defines a node"""
    def __init__(self, data, next_node=None):
        """initializes the node with instance variables"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set the data attribute"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute
        Returns: The next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the value of next node"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """This here is a singly-linked list"""
    def __init__(self):
        """Initialize the list"""
        self.head = None

    def __str__(self):
        """Print the list"""
        print_list = ""
        where = self.head
        while where:
            print_list += str(where.data) + "\n"
            where = where.next_node
        return print_list[:-1]

    def sorted_insert(self, value):
        """Inserting into a sorted list
        Args:
            value: Final value
        """
        new_list = Node(value)
        if not self.head:
            self.head = new_list
            return
        if value < self.head.data:
            new_list.next_node = self.head
            self.head = new_list
            return
        where = self.head
        while where.next_node and where.next_node.data < value:
            where = where.next_node
        if where.next_node:
            new_list.next_node = where.next_node
        where.next_node = new_list
