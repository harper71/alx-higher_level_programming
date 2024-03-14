#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv) - 1
    if argv == 0:
        print("{} arguments.".format(argv))
    else:
        print("{} arguments:".format(argv))
        for i in range(1, argv + 1):
            names = sys.argv[i]
            print("{}: {}".format(i, names))
