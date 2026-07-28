students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

max_scorer = students[0]
class_avg = 0
subject_set = set()
high_scorers = []

for student in students:
    if student["score"] > max_scorer["score"]:
        max_scorer = student
        
    class_avg += student["score"]
    subject_set.add(student["subject"])
    
    if student["score"] > 75:
        high_scorers.append(student["name"])
        
class_avg /= len(students)

print(f'Top scorer:       {max_scorer["name"]} ({max_scorer["score"]})')
print(f"Class average:    {class_avg:.1f}")
print(f"Subjects offered: {subject_set}")
print(f"High scorers:     {high_scorers}")