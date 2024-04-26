#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    chr = "" if len(sys.argv) == 1 else sys.argv[1]
    x = {"q": chr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=x)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
