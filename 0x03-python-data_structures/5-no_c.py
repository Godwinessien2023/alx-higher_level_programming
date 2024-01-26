#!/usr/bin/python3
def no_c(my_string):
    without_c = ""
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            without_c += my_string[i]
    return (without_c)
