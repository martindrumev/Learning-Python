# Exercise
'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''


# My code
import datetime
today = datetime.date.today()
print(today)


# Answer
'''
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
'''