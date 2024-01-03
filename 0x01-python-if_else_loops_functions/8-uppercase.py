#!/usr/bin/python3
def uppercase(str):
    for i in str:

        if (ord(i) > 96 and ord(i) < 123):
            new = ord(i) - 32
            print("{}".format(chr(new)), end="")
        else:
            print("{}".format(i), end="")
    

