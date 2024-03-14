#!/usr/bin/python3
import sys
if __name__ == "__main__":
    values = len(sys.argv) - 1
    if values == 0:
        print("{}: arguments".format(values))
    else:
        print("{} arguments:".format(values))
        for i in range(1, values + 1):
            names = sys.argv[i]
            print("{}: {}".format(i, names))
