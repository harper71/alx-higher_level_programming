#!/usr/bin/python3
import sys

values = len(sys.argv) - 1
if values == 0:
    print(f"{values}: arguments")
else:
    print(f"{values} arguments:")
    for i in range(1, values + 1):
        names = sys.argv[i]
        print(f"{i}: {names}")
