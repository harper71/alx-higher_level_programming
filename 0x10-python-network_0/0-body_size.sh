#!/bin/bash
# send a request to URL

if [ -z "$1" ];
then
    echo "usage: $0 <URL>"
    exit 1
fi

URL="$1"

response=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo "$response"
