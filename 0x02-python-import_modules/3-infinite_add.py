#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]

    nums = [int(argc) for argc in args]

    total_sum = 0

    if len(args) > 1:
        for i in nums:
            total_sum += i

    print("{}".format(total_sum))
