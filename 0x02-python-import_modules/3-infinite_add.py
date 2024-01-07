#!/usr/bin/python3

def sum_args(*args):
    try:
        total = sum(int(arg) for arg in args)
        print(total)
    except ValueError:
        print("Error")

if __name__ == "__main__":
    import sys
    sum_args(*sys.argv[1:])

