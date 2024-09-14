import re


def is_integer(string):

    return string.isdigit()

input_str = input("Input a string:")

if is_integer(input_str):
    print("The string is  an integer")
else:
    print("The string is not an integer")