file = open("17data", "r")
print(file.read())
print()

file = open("17data", "r")
print(file.readline())
print()

# Creating a list
file = open("17data", "r")
print(file.readlines())
print()

file.close()

###

# It will be manually closed
with open("17data", "r") as file:
    print(file.read())
    print()

with open("17data", "r") as file:
    for line in file:
        print(line.strip("\n"))