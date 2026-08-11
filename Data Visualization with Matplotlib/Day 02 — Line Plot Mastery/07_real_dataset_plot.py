import matplotlib.pyplot as plt
import csv

"""
REAL DATASET PLOTTING
---------------------
We read data from CSV and plot it.
"""

months = []
sales = []
profit = []

# Open CSV file
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        sales.append(int(row["sales"]))
        profit.append(int(row["profit"]))

# Plot Sales
plt.plot(months, sales, marker="o", label="Sales", linewidth=2)

# Plot Profit
plt.plot(months, profit, marker="o", label="Profit", linewidth=2)

plt.title("Monthly Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.show()