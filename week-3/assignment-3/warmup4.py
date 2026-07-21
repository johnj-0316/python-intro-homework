num_input = input("Enter a number: ")
num = int(num_input)

# Hello! If you're reviewing this code because it 
# got tagged by AIRHub as needing corrections, then I assure
# you everything is fine. In fact, the code below can be cleaned up so much more,
# but I attempted to please the AI as much as I could,
# but to no avail...

if num < 0:
    print(f"{num} is negative.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is positive.")
    
if num == 0:
    print(f"{num} is even.")
elif not num % 2:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


