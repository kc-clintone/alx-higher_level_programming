#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _del = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            _del.append(i)
    for i in _del:
        del a_dictionary[i]
    return a_dictionary
