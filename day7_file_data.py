expenses = []

file = open("expenses.txt", "r")
for line in file:
    expenses.append(float(line.strip()))
file.close()
total = sum(expenses)
average = total / len(expenses)
print("Expenses:", expenses)
print("Total:", total)
print("Average:", average)
print("Highest:", max(expenses))
print("Lowest:", min(expenses))
