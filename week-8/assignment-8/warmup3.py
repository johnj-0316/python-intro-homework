try:
    with open("../data/missing.txt") as file:
        pass
except FileNotFoundError as err:
    print("Error: \"missing.txt\" was not found. Please check the file path and try again.")