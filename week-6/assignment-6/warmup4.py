def is_valid_score(score: int) -> bool:
    return score >= 0 and score <= 100

user_input = input("Enter a score: ")

if user_input.isdigit() and is_valid_score(int(user_input)):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")