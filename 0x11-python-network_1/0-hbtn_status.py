#!/usr/bin/python3

from urllib import request

try:
    with request.urlopen("https://alx-intranet.hbtn.io/status") as URL_0:
        response = URL_0.read()
        print("Body response:")
        print("\t- type:", type(response))
        print("\t- content:", response)
        print("\t- utf8 content:", response.decode('utf-8'))
except Exception as e:
    print(e)
