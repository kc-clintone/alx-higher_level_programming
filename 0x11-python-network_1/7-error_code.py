#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the
response body.
Usage: ./7-error_code.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    target = sys.argv[1]

    req = requests.get(target)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
