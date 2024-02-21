#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    all = 0
    digs = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        roman_n = digs[roman]
        all += roman_n if all < roman_n * 5 else -roman_n
    return all
