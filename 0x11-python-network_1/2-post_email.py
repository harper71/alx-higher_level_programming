import urllib.request, urllib.parse
import sys
"""
gets heade value
"""

URL = sys.argv[1]
email = sys.argv[2]

value = {'email': email}

encode_data = urllib.parse.urlencode(value).encode('utf-8')

request = urllib.request.Request(URL, data=encode_data, method='POST')


with urllib.request.urlopen(request) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))

