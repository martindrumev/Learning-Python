# Exercise
'''
WWrite a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''


# My code
import datetime

print(datetime.datetime.now())

#Stackoverflow
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Answer
'''
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
'''