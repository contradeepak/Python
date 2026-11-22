# generate_report.py

student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

subjects = ["Math", "Science", "English", "History", "Computer"]
marks = {}
total = 0

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks[subject] = score
    total += score

average = total / len(subjects)

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

status = "Pass" if average >= 40 else "Fail"

# HTML structure
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Report Card - {student_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 40px;
        }}
        .report {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            width: 500px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}
        h2 {{
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        .summary {{
            margin-top: 20px;
        }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
    </style>
</head>
<body>
    <div class="report">
        <h2>Student Report Card</h2>
        <p><strong>Name:</strong> {student_name}</p>
        <p><strong>Roll Number:</strong> {roll_number}</p>
        <table>
            <tr><th>Subject</th><th>Marks</th></tr>
"""

for subject, score in marks.items():
    html_content += f"<tr><td>{subject}</td><td>{score}</td></tr>\n"

html_content += f"""
        </table>
        <div class="summary">
            <p><strong>Total Marks:</strong> {total}</p>
            <p><strong>Average:</strong> {average:.2f}</p>
            <p><strong>Grade:</strong> {grade}</p>
            <p><strong>Status:</strong> <span class="{status.lower()}">{status}</span></p>
        </div>
    </div>
</body>
</html>
"""

# Write to HTML file
with open("report_card.html", "w") as file:
    file.write(html_content)

print("✅ Report card generated as 'report_card.html'")
