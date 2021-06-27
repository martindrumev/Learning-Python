lines = ["This is line 1. \n", "This is line 2."]

# Mode "a" will append
with open("17data", "w") as file:
    file.write("Hello, world!")

with open("17data", "w") as file:
    file.writelines(lines)

print()

employee_file = open("16index.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()