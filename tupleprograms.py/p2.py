# Unpacking tuples in loop

records = [(1, "Math", 80), (2, "Science", 85), (3, "English", 95)]
for roll, subject, marks in records:
    print(f"Roll {roll} scored {marks} in {subject}")