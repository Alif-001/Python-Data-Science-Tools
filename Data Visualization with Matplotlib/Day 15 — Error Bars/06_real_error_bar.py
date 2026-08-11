import matplotlib.pyplot as plt
import csv

"""
REAL DATA ERROR BAR
-------------------
We visualize experimental results with uncertainty.
"""

trial = []
value = []
error = []

# Read CSV file
with open("experiment_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        trial.append(int(row["trial"]))
        value.append(int(row["value"]))
        error.append(float(row["error"]))

# Create error bar plot
plt.errorbar(
    trial,
    value,
    yerr=error,
    fmt='o',
    capsize=5,
    color="blue"
)

plt.title("Experiment Results with Error Bars")
plt.xlabel("Trial")
plt.ylabel("Value")

plt.show()