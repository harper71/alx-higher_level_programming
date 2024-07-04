#!/bin/bash
# uses the get command
curl -s -o /dev/null -w "%{http_code}" "$1" && curl -s "$1"