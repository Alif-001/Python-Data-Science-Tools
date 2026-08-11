import matplotlib.pyplot as plt
import csv

"""
REAL PROFESSIONAL STYLE CHART
-----------------------------
We apply styling to real business data.
"""

years = []
revenue = []
profit = []

# Read CSV file
with open("company_growth.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        years.append(row["year"])
        revenue.append(int(row["revenue"]))
        profit.append(int(row["profit"]))

# Professional style
plt.style.use("ggplot")

plt.figure(figsize=(8, 4))

# Revenue line
plt.plot(years, revenue, marker="o", label="Revenue", linewidth=3)

# Profit line
plt.plot(years, profit, marker="s", label="Profit", linewidth=3)

# Styling
plt.title("Company Growth Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Amount", fontsize=12)

plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()