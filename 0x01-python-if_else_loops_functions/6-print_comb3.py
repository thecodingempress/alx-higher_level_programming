#!/usr/bin/python3

for i in range(0,10):
    for y in range(0, 10):
        if i == y::
            continue
        print("{}{}".format(i, y), end=", ")
