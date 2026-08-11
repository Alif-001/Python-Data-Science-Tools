import matplotlib.pyplot as plt
import csv

"""
REAL WORLD PIE CHART
--------------------
We visualize market share of companies.
"""

companies = []
shares = []

# Read CSV file
with open("market_share.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        companies.append(row["company"])
        shares.append(int(row["share"]))

# Custom colors
colors = ["gold", "skyblue", "lightgreen", "orange", "lightgray"]

plt.pie(
    shares,
    labels=companies,
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
    shadow=True
)

plt.title("Market Share Distribution")

plt.show()