#!/usr/bin/python3
for ord(c) in range(97, 123):
    if ord(c) % 2 == 0:
        print("{}".format(chr(ord(c))), end="")
    else:
        print("{}".format(chr(ord(c)) - 32), end="")
