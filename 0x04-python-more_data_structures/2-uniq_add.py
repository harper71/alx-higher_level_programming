#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set()
    for index, i in enumerate(my_list):
        if i not in unique_elements:
            unique_elements.add(i)
    return sum(unique_elements)
