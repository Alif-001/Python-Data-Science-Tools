import matplotlib.pyplot as plt
import csv

"""
REAL STORYTELLING VISUALIZATION
-------------------------------
We highlight growth points using annotations.
"""

months = []
sales = []
profit = []

# Read CSV file
with open("sales_growth.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        sales.append(int(row["sales"]))
        profit.append(int(row["profit"]))

plt.plot(months, sales, marker="o", label="Sales")
plt.plot(months, profit, marker="s", label="Profit")

# Highlight peak sales
max_index = sales.index(max(sales))

plt.scatter(months[max_index], sales[max_index], color="red", s=100)

plt.annotate(
    "Highest Sales",
    xy=(months[max_index], sales[max_index]),
    xytext=(1, 250),
    arrowprops=dict(arrowstyle="->", color="red")
)

plt.title("Sales Growth Storytelling")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()

plt.show()