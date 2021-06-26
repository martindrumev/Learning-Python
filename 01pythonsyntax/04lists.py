numbers = [10, 20, 30]
print(numbers)
print(numbers[0])

mylist = [10, "John", 30]
print(mylist)

mylist[0] += 1
print(mylist)

print()
lucky_numbers = [4, 8, 44, 34, 44, 84]
friends = ["Mark", "John", "Richard", "John"]
#friends.extend(lucky_numbers)
friends.append("Ilias")
friends.insert(1, "Kelly")
friends.remove("Mark")
friends.pop()
print(friends.count("John"))
print(friends.index("Richard"))
print()
friends.sort()
print(friends)
print()

friends2 = friends.copy()

friends.clear()
print(friends)

