with open("../data/notes.txt", "r") as file:
    lines = file.readlines()
    
    for line in range(len(lines)):
        print(f"Line {line + 1}: {lines[line].strip()}");