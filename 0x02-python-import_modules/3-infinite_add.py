#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    num = len(argv)
    if num == 1:
        print(0)
    else:
        total = 0
        for i in argv[1:]:
            total += int(i)
        print(total)
