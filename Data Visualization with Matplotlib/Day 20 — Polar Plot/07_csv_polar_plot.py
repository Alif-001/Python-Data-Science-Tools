import numpy as np
import matplotlib.pyplot as plt
import csv

"""
CSV BASED POLAR PLOT
--------------------
We read angle + value from dataset.
"""

angles = []
values = []

# Read CSV file
with open("polar_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Convert degree → radians
        angles.append(np.deg2rad(float(row["angle"])))
        values.append(float(row["value"]))

plt.subplot(111, projection='polar')

plt.plot(angles, values, marker='o')
plt.fill(angles, values, alpha=0.3)

plt.title("Polar Plot from CSV Data")

plt.show()