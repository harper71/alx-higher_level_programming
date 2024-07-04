#!/bin/bash
# uses the get command
response=$(curl -s -o /dev/null -w "%{http_code}" "$URL") && echo "$response"
