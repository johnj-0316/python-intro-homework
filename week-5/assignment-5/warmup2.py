user_input = input("Enter a positive integer: ")

while not user_input.isdigit() or int(user_input) <= 0:
    print("That's not a positive integer. Try again.")
    user_input = input("Enter a positive integer: ")

print(f"Got it: {user_input}")