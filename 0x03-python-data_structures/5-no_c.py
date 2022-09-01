#!/usr/bin/env python3
def no_c(my_string):
    for x in my_string:
        if x == 'c' and x == 'C':
            my_string.replace(x, '')
