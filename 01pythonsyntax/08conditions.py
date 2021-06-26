age = 13

if age == 10:
    print("This is 10.")
elif age == 12:
    print("This age is 12")
else:
    print("hello")

is_male = True
is_female = True

if is_male or is_female:
    print("You are a male/female")
elif is_male and not(is_female):
    print("You are Male")
else:
    print("You are female")

print()

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(355, 40, 5))