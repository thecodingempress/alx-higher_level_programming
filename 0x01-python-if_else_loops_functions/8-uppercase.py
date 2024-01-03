#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:

        if (ord(i) > 96 and ord(i) < 123):
            i = chr(ord(i) - 32)
        upper += i
    print("{}".format(upper))
