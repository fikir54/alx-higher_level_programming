#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list[:]
    del new_list[idx]
    new_list.insert(idx, element)
    return new_list 
