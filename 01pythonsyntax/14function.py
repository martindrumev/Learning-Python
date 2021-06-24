# def = define
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