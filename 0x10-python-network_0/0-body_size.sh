#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
#and displays the size of the body of the response

# Check if URL is passed
if [ -z "$1" ]; then
    echo "URL missng: Usage: $0 URL"
    exit 1
fi

# Send request to the URL and get response size
res=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the response size
echo "$res"
