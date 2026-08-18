import os
import csv
import datetime

expenses_path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(expenses_path):
    raise Exception("There was an error opening the expenses.csv file.")

with open(expenses_path) as csvfile:
    expenses_dicts = list(csv.DictReader(csvfile))
    
    for row in expenses_dicts:
        row["amount"] = float(row["amount"])
        
    food_dicts = [row for row in expenses_dicts if row["category"] == "Food"]
    total_spent = 0
    
    for row in food_dicts:
        total_spent += float(row["amount"])
        
    food_report_path = os.path.join("..", "data", "food_report.txt")
    
    with open(food_report_path, "w") as food_report:
        expenses = "\n".join(list(map(lambda data: f"{data['date']}: ${data['amount']}", food_dicts)))
        food_report.write(
        f"""Food Expense Report — generated {datetime.datetime.now().strftime("%B %d, %Y")}
{expenses}
Total: ${total_spent:.2f}   
         """
        )
    