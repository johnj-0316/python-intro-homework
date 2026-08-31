num1 = input("Enter the numerator: ")
num2 = input("Enter the denominator: ")

try:
    f1 = float(num1)
    f2 = float(num2)
    quot = f1 / f2
    print(f"{f1} ÷ {f2} = {quot}")
except ValueError as value_err:
    print("One of the inputs is not a valid number.")
except ZeroDivisionError as err:
    print("Can't divide by zero — please try a non-zero denominator.")
    