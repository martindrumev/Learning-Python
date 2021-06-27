from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Caytlin", "Art", 2.5, True)
student3 = Student("Mark", "Art", 4.5, True)

print(student1.name)
print(student2.name)
print(student1.gpa)

print(student3.on_honor_roll())