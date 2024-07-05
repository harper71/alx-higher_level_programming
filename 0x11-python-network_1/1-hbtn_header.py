#!/usr/bin/python3
import urllib.request
import sys
"""
gets heade value
"""

URL = sys.argv[1]

with urllib.request.urlopen(URL) as response:
    head_value = response.getheader('X-Request-Id')
    print(head_value)
