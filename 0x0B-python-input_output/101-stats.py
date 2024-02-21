#!/usr/bin/python3
"""This module contains a function that reads from standard input and
   computes the metrics
"""

def print_stats(size, status_codes):
    """This prints available metrics"""
    print("File size: {}".format(size))
    for i in sorted(status_codes):
        print("{}: {}".format(i, status_codes[i]))
if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    try:
        for x in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1
            x = x.split()
            try:
                size += int(x[-1])
            except (IndexError, ValueError):
                pass
            try:
                if x[-2] in valid_codes:
                    if status_codes.get(x[-2], -1) == -1:
                        status_codes[x[-2]] = 1
                    else:
                        status_codes[x[-2]] += 1
            except IndexError:
                pass
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
