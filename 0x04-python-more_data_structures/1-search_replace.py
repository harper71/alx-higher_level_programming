#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_list = []
    for item in my_list:
        if item == search:
            replace_list.append(replace)
        else:
            replace_list.append(item)
    return replace_list
