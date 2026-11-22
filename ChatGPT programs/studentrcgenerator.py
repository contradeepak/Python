# Student Report Card Generator

# Step 1: Take basic info
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Step 2: Subjects and marks (as list and dict)
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = {}

for subject in subjects:
    score = float(input(f"Enter marks for {subject} (out of 100): "))
    marks[subject] = score

# Step 3: Calculate total, average, and grade
total_marks = sum(marks.values())
average = total_marks / len(subjects)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

# Step 4: Passed or not (boolean)
is_passed = average >= 40

# Step 5: Display Report Card
print("\n========== REPORT CARD ==========")
print(f"Name       : {student_name}")
print(f"Roll No.   : {roll_number}")
print("---------------------------------")
for subject, score in marks.items():
    print(f"{subject:10}: {score}")
print("---------------------------------")
print(f"Total      : {total_marks}")
print(f"Average    : {average:.2f}")
print(f"Grade      : {grade}")
print(f"Result     : {'Pass' if is_passed else 'Fail'}")
print("=================================")
