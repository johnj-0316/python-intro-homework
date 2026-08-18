with open("../data/notes.txt", "r") as file:
    line_num = 1    
    for line in file:
        print(f"Line {line_num}: {line.strip()}")
        line_num += 1