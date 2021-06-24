lines = ["This is line 1. \n", "This is line 2."]

with open("17data", "w") as file:
    file.write("Hello, world!")

with open("17data", "w") as file:
    file.writelines(lines)