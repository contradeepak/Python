# Sort tuples by multiple keys

students = [
    ("Alice", 22, 95),
    ("Bob", 20, 50),
    ("Charlie", 22, 92),
    ("Dev", 30, 50)

]

sorted_students = sorted(students, key=lambda x: (x[2], x[1]))
print("Sorted students:", sorted_students)
