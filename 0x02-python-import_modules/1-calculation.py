#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

# define variables for a and b
    a = 10
    b = 5

    addition = add(a, b)
    minus = sub(a, b)
    multiply = mul(a, b)
    division = div(a, b)
# print answers
    print(f"a + b = {addition :d}")
    print(f"a - b = {minus :d}")
    print(f"a * b = {multiply :d}")
    print(f"a / b = {division :d}")
