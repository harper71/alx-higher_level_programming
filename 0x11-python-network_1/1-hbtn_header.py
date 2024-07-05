#!/usr/bin/python3
import urllib.request
import sys
"""
gets heade value
"""

URL = sys.argv[1]


def fetch_request_id(url):
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        request_id = dict(headers).get('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print('X-Request-Id header not found')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        fetch_request_id(url)
