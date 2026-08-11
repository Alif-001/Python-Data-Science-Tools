import matplotlib.pyplot as plt
import csv

"""
CSV BASED VISUALIZATION
----------------------
We use same dataset for:
- stem plot
- step plot
"""

time = []
value = []

# Read CSV
with open("signal_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        time.append(int(row["time"]))
        value.append(int(row["value"]))

# Convert to lists
x = time
y = value

# ---------------- STEM PLOT ----------------
plt.subplot(1, 2, 1)
plt.stem(x, y)
plt.title("Stem Plot")

# ---------------- STEP PLOT ----------------
plt.subplot(1, 2, 2)
plt.step(x, y, where="mid")
plt.title("Step Plot")

plt.show()