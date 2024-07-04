#!/bin/bash
# send a request to URL
response=$(curl -s -o /dev/null -w '%{size_download}' "$1") && echo "$response"
