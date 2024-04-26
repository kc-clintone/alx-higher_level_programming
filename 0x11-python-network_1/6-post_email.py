#!/usr/bin/python3
"""
This script sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    uri = sys.argv[1]
    x = {"email": sys.argv[2]}
    req = requests.post(uri, data=x)
    print(req.text)
