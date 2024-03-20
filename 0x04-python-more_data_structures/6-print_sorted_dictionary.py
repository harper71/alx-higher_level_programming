#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorting = sorted(a_dictionary.keys())
    for items in sorting:
        print("{}: {}".format(items, a_dictionary[items]))
