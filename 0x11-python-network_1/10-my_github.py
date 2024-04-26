#!/usr/bin/python3
"""
This script uses the GitHub API to display a GitHub ID
based on given credentials.
Usage:
    ./10-my_github.py <GitHub username> <GitHub ID>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authenticate = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get("https://api.github.com/user", auth=authenticate)
    print(request.json().get("id"))
