import csv;

with open("../data/students.csv") as csvfile:
    csv_dict = csv.DictReader(csvfile)
    
    for row in csv_dict:
        print(f"{row['name']}: {row['score']}")