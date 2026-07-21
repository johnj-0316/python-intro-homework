num_input = input("Enter a number: ")
num = int(num_input)

if num == 0:
    print(f"{num} is zero.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is positive.")
    
if num == 0:
    print(f"{num} is even.")
elif not num % 2:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

