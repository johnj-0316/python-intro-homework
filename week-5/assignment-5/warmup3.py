names_list = ["James", "Zack", "Eris", "Marcus", "Babel"]
user_input = input("Enter a name to search for: ")


for i in range(len(names_list)):
    if names_list[i].lower() == user_input.lower():
        print(f"Found \"{user_input}\" at index {i}.")
        break
    elif i == len(names_list) - 1:
        print(f"\"{user_input.capitalize()}\" was not found in the list.")


    