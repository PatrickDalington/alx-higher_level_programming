#!/usr/bin/python3

def no_c(my_string):
    new = ''
    for xter in my_string:
        if xter in "Cc":
            continue
        new += xter
    return new
