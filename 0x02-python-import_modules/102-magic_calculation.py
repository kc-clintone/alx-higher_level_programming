#!/usr/bin/python3
def magic_calculation(i, j):
    add, sub = __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).add, __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).sub

    if i < j:
        x = add(i, j)
        for i in range(4, 6):
            x = add(x, k)
        return x
    else:
        return sub(i, j)
