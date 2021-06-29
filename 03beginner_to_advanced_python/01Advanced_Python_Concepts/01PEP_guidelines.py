# Always import on separated lines
import os
import sys

# Importing from a module it's okay to be on one line separated by comma
from MyModule import foo, bar, foobar


def my_function(one, two,
                three, four,
                five, six):
    print("Hello World")

# Between two functions you need 2 lines, same goes for classes
def second_function():
    print("Second function")


my_list = [1, 2,
           3, 4,
           5, 6]

# Keep the low priority with white space
x = 3*52 + 7*2

