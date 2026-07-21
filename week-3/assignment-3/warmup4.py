num_input = input("Enter a number: ")
num = int(num_input)

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")
    
if num % 2 == 1:
    print(f"{num} is odd.")
elif num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is even.")

