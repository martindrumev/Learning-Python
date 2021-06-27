class Chef:

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_spacial_dish(self):
        print("The chef makes a bbq ribs")

# Inheritance
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_spacial_dish(self):
        print("The chef makes a orange chicken")


myChef = Chef()
myChef.make_salad()

myChineseChef = ChineseChef()
myChineseChef.make_spacial_dish()