import os

print(f"Current working directory: {os.getcwd()}")

expenses_exists = os.path.exists("../data/expenses.csv")

if expenses_exists:
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    
joined_path = os.path.join("..", "data", "expenses.csv")
print(joined_path)