while True:
    try:
        num = float(input("Enter a number: "))
        print(f"You entered: {num}")
        break
    except ValueError as err:
        print(f"That's not a valid number. Try again.")