#!/usr/bin/python3
if __name__ == " __main__":
    import calculator_1
# define variables for a and b
    a = 10
    b = 5
# represent each calculation
    sum_result = calculator_1.add(a, b)
    sub_result = calculator_1.sub(a, b)
    mul_result = calculator_1.mul(a, b)
    div_result = calculator_1.div(a, b)
# print answers
    print(f"a + b = {sum_result}")
    print(f"a - b = {sub_result}")
    print(f"a * b = {mul_result}")
    print(f"a / b = {div_result}")
