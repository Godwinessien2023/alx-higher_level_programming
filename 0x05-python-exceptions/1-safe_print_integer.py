#!/usr/bin/python3

def safe_print_integer(value):
    try:
        for i in range(len(value)):
            if isdigit(value[i], int):
                print("{:d}".format(value[i]), end="")
        print() 
        return True
    except ValueError:
        print()
        return False
