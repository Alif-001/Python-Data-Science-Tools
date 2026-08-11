import matplotlib.pyplot as plt
import csv

"""
REAL DATASET BOX PLOT
---------------------
We analyze salary distribution by department.
"""

it = []
hr = []
sales = []

# Read CSV file
with open("employee_salary.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = int(row["salary"])

        if row["department"] == "IT":
            it.append(salary)
        elif row["department"] == "HR":
            hr.append(salary)
        elif row["department"] == "Sales":
            sales.append(salary)

# Combine data
data = [it, hr, sales]

plt.boxplot(data)

plt.xticks([1, 2, 3], ["IT", "HR", "Sales"])

plt.title("Salary Distribution by Department")
plt.ylabel("Salary")

plt.show()