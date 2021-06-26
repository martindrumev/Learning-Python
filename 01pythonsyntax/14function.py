# def = define
# def = function
def square(num):
    return num ** 2

print(square(10))

def names(first, last):
    return first + " " + last

print(names("John", "Steven"))


print()

mylist = [1, 2, 3, 4, 5]

def print_elements(list1):
    for e in list1:
        print(e)

print_elements(mylist)
print()

def say_hi(name):
    print("Hello " + name)
say_hi("Mike")

# 2 or more words we use in python _ underscore

