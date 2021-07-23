# Exercise
'''
Write a Python program to get the Python version you are using.
'''


# My code
import sys

print(sys.version)

# Answer
'''
import platform
print(platform.python_version())

------------------------------------

import platform
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
'''