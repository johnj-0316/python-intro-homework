try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    quot = num1 / num2
    print(f"{num1} ÷ {num2} = {quot}")
except ZeroDivisionError as err:
    print("Can't divide by zero — please try a non-zero denominator.")
    