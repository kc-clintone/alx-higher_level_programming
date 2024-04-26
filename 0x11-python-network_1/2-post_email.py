#!/usr/bin/python3
"""
This script sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    uri = sys.argv[1]
    x = {"email": sys.argv[2]}
    y = urllib.parse.urlencode(x).encode("ascii")

    req = urllib.request.Request(uri, y)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
