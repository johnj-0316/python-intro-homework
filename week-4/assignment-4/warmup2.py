student_dict = {
    "name": "John",
    "grade": 96,
    "subjects": ["CS 201", "Stats 101", "Cooking 102"]
}

for key, value in student_dict.items():
    print(f"{key}:", value)
    
student_dict["graduated"] = False

for key, value in student_dict.items():
    print(f"{key}:", value)