#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from each tuple)
    a_first = tuple_a[0] if len(tuple_a) >= 1 else 0
    a_second = tuple_a[1] if len(tuple_a) >= 2 else 0
    b_first = tuple_b[0] if len(tuple_b) >= 1 else 0
    b_second = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Perform the addition
    result_first = a_first + b_first
    result_second = a_second + b_second

    # Return the result as a tuple
    return (result_first, result_second)
