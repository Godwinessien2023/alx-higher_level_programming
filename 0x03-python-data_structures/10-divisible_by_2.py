#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    # Itterate my_list
    new_list = []

    # evaluation statements to show divisible by 2
    for i in my_list:
        if i % 2 == 0:
            my_list.append(True)
        else:
            my_list.append(False)

    return new_list
