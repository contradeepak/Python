# Assignment to print Records and Values

student_records = {}
no_of_students = 3

for i in range(no_of_students):
    name = input("Enter the student's name: ")
    marks = int(input("Enter the student's marks: "))
    student_records[name] = marks

print(student_records)




# How can you print only marks

student_records = {}
no_of_students = 3

for i in range(no_of_students):
    name = input("Enter the student's name: ")
    marks = int(input("Enter the student's marks: "))
    student_records[name] = marks

# Print only student names
    for student in student_records.keys():
    print(student)
