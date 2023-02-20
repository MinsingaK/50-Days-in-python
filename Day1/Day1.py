# we import math module to use sqrt method

from math import *

def square_or_root():
    number = int(input("Entrer un nombre : "))
    if number%5 == 0:
        return sqrt(number)
    else:
        rest = number%5
        return rest

print(square_or_root())