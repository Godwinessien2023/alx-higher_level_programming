#!/usr/bin/python3

import random
import math

randList = ["String", 1.234, 28, "Tolani", "Toni", "Healer"]
oneToTen = list(range(10))

randList = randList + oneToTen
print(randList[0])

print("list length :", len(randList))

first3 = randList[0:3]
print(first3)

first7 = randList[0:7]
print(first7)

first12 = randList[0:12]
print (first12)

for i in first3:
	print("{} : {}" .format(first3.index(i), i))

print(first3 [0] * 3)

print("index of string:", first3.index("String"))

print("how many String:", first3.count("String"))

first3.append("Another Life")

for i in first3:
        print("{} : {}" .format(first3.index(i), i))
