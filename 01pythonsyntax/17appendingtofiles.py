with open("17data", "a") as file:
    file.write("\nHello, world!")

lines = ["\nThis is line 4.\n", "This is line 5."]

with open("17data", "a") as file:
    file.writelines(lines)