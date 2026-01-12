# Day 6 - Simple Expense Tracker 

expenses = []
days = int(input("Enter number of days: "))
for i in range(days):
    amount = float(input(f"Enter expense for day {i+1}: "))
    expenses.append(amount)
total_expense = sum(expenses)
avg_expenses=total_expense/days
print("\nExpense Summary")
print("Total expense:", total_expense)
if (avg_expenses>=1000):
  print("you are spending too much money")
else:
  print('you are on track')
  

