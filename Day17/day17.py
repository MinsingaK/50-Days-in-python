from random import *


def user_name():
    name = input("Enter your name : ").lower()
    name2 = name[::-1]
    n = str(randint(0,10))
    username = name2 + n
    return print(f"your username is {username}")


user_name()