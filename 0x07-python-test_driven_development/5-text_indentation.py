#!/usr/bin/python3
"""
This module contains a function that prints a text with 2
new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that indicate a new line
    new_line_chars = ['.', '?', ':']

    # Empty line
    current_line = ""

    for char in text:
        if char in new_line_chars:
            print(current_line.strip())
            current_line = ""
        else:
            current_line += char
    print(current_line.strip())

