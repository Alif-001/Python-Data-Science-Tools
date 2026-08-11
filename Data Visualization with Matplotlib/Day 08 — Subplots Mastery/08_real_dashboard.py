import matplotlib.pyplot as plt
import csv

"""
REAL DASHBOARD WITH SUBPLOTS
----------------------------
We visualize business data (sales + ads).
"""

months = []
online = []
offline = []
ads = []

# Read CSV file
with open("sales_dashboard.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        online.append(int(row["online"]))
        offline.append(int(row["offline"]))
        ads.append(int(row["ads"]))

# Create dashboard layout
fig, ax = plt.subplots(2, 2, figsize=(10, 6))

# Line charts
ax[0, 0].plot(months, online, label="Online", color="blue")
ax[0, 0].set_title("Online Sales")

ax[0, 1].plot(months, offline, label="Offline", color="green")
ax[0, 1].set_title("Offline Sales")

# Bar chart
ax[1, 0].bar(months, ads, color="orange")
ax[1, 0].set_title("Ad Spend")

# Comparison chart
ax[1, 1].plot(months, online, label="Online")
ax[1, 1].plot(months, offline, label="Offline")
ax[1, 1].set_title("Comparison")
ax[1, 1].legend()

plt.tight_layout()

plt.show()