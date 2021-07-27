# Exercise
'''
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
'''


# My code
input = input("Filename: ")
output = input.split(".")

print(output[1])

# Answer
'''
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
'''