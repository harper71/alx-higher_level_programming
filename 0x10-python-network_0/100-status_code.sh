#!/bin/bash
# checks the status code of URL
curl -s -o /dev/null -w "%{http_code}" "$1"
