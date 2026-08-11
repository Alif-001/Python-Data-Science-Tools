import matplotlib.pyplot as plt
import csv

"""
REAL DATA + AXIS CUSTOMIZATION
-----------------------------
We use real business metrics.
"""

months = []
revenue = []
users = []

# Read CSV file
with open("company_metrics.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        revenue.append(int(row["revenue"]))
        users.append(int(row["users"]))

plt.plot(months, revenue, marker="o", label="Revenue")

# Rotate X-axis labels (important for readability)
plt.xticks(rotation=45)

# Axis limits
plt.ylim(0, 9000)

# Scientific notation (useful for large values)
plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

plt.title("Company Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()

plt.show()