"Complex structure with all data type"


person = {
    "name": "Rahul",
    "age": "30",
    "is_student": False,
    "skills": ["Python", "SQL"],
    "education": ("BSC", "MCA"),
    "scores": {"math": 88, "english": 92},
    "hobbies": {"reading", "cycling" }


}

print("Person Info:")
for key, value in person.items():
    print(f"{key} ({type(value)}): {value}")