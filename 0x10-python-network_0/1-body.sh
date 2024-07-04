#!/bin/bash
# uses the get command
curl -s -o /tmp/body.txt -w "%{http_code}" "$1" && cat /tmp/body.txt
