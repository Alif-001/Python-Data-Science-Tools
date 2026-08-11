import matplotlib.pyplot as plt
import csv

"""
REAL STACK + AREA VISUALIZATION
------------------------------
We visualize company product growth.
"""

months = []
product_a = []
product_b = []
product_c = []

# Read CSV file
with open("company_growth_area.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        product_a.append(int(row["product_a"]))
        product_b.append(int(row["product_b"]))
        product_c.append(int(row["product_c"]))

# Stack plot (area visualization)
plt.stackplot(
    months,
    product_a,
    product_b,
    product_c,
    labels=["Product A", "Product B", "Product C"],
    alpha=0.7
)

plt.title("Company Product Growth (Stacked Area)")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()