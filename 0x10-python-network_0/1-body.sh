#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[ -z "$1" ] && echo "Usage: $0 URL" && exit 1;curl -s -o /dev/null -w "%{size_download}" "$1"
