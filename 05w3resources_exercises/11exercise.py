# Exercise
'''
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''


# My code
input = input("Absolute value of: ")
absolute = abs(int(input))
print(absolute)


# Answer
'''
print(abs.__doc__)

'''