age_input = input("Enter your age: ")
age = int(age_input)

if age >= 65:
    print("You are a Senior.")
elif age < 65 and age >= 18:
    print("You are an Adult.")
elif age < 18 and age >= 13:
    print("You are a Teen.")
else:
    print("You are a Child.")
    
