#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for n in range(0, list_length):
        try:
            q = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            q = 0
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            final_list.append(q)
    return (final_list)
