#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        x = 0
        d = 0
        for tuple in my_list:
            x += (tuple[0] * tuple[1])
            d += (tuple[1])
        return (x/d)
    return 0
