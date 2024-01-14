#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for m, num in enumerate(row):
            if m != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
