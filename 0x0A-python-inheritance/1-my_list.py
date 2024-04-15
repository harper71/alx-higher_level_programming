#!/usr/bin/python3
""" creates a list"""


class MyList(list):
    """prints a sorted list

    Args:
        list (int): most be an int
    """

    def print_sorted(self):
        sorted_list = sorted(self)

        print("{}".format(sorted_list))
