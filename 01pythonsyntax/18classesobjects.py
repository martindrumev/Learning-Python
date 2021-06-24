class Human():
    name = "John"
    age = 10

    def hello(self):
        print("Hello, world!")

human = Human()

human.hello()
print()


class Undead():
    def __init__(self, name, age):
        print("Object created!")
        self.name = name
        self.age = age

# This function it will be called when you try to print that object
    def __str__(self):
        return "Printed Object!"

undead = Undead("Rick", 10)

print(undead.name)
print(undead.age)
print(undead)
print()

# This will get all value from class Human
class Orc(Undead):
    # this will overwrite from the Human class
    def __str__(self):
        return "Orc created!"

human = Undead("Leilan", 30)
orc = Orc("Draktar", 20)

print(undead.name)
print(undead.age)
print()

print(orc.name)
print(orc.age)
print(orc)


