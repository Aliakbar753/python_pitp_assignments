students = {
    'Ali' : 80,
    'sara': 90,
    'Ahmed' : 75
}

#shows students name
print(students.keys())

#shows marks of students
print(students.values())

maximum = max(students.values())
for i in students:
    if maximum == students.get(i):
        print(f"{i} has the highest marks = {maximum}")
    