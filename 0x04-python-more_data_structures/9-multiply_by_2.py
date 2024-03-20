#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_dict = {}
    for key, item in a_dictionary.items():

        mult_dict[key] = item * 2
    return mult_dict
