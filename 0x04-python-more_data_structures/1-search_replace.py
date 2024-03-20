#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_list = []
    replace_list.extend(my_list)
    replace_list[search - 1] = replace
    return replace_list
