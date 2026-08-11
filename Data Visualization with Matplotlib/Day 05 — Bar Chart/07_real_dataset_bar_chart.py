import matplotlib.pyplot as plt
import csv
import numpy as np

"""
REAL DATASET BAR CHART
----------------------
We compare multiple products over time.
"""

months = []
product_a = []
product_b = []
product_c = []

# Read CSV file
with open("company_sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        product_a.append(int(row["product_a"]))
        product_b.append(int(row["product_b"]))
        product_c.append(int(row["product_c"]))

# X positions
x = np.arange(len(months))
width = 0.25

# Grouped bars
plt.bar(x - width, product_a, width, label="Product A")
plt.bar(x, product_b, width, label="Product B")
plt.bar(x + width, product_c, width, label="Product C")

plt.xticks(x, months)

plt.title("Monthly Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()