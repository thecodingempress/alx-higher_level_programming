#!/usr/bin/python3

def uniq_add(my_list):
    newly = set(my_list)

    newlist = list(newly)

    sum = 0

    for i in range(len(newlist)):
            sum = sum + newlist[i]

    return sum
