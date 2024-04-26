#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    uri = sys.argv[1]
    req = urllib.request.Request(uri)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
