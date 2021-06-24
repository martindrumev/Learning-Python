age = 10

if age == 10:
    pass

numbers = [1, 2, 3, 4, 5]

for e in numbers:
    if e == 3:
        continue
    print(e)

print()

for e in numbers:
    if e == 3:
        break
    print(e)