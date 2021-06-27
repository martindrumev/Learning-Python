num = input("Enter a number: ")

try:
    num = int(num)
except:
    pass

print(num)

print()

try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10 /0
except ValueError as err:
    print(err)
except ZeroDivisionError:
    print("Divided by zero")