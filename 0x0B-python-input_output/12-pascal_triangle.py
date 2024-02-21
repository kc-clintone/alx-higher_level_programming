#!/usr/bin/python3
"""This module defines the famouse Pascal's Triangle function"""


def pascal_triangle(n):
    """This function represents Pascal's Triangle of size n"""
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        trio = tri[-1]
        temp = [1]
        for index in range(len(trio) - 1):
            temp.append(trio[index] + trio[index + 1])
        temp.append(1)
        tri.append(temp)
    return tri
