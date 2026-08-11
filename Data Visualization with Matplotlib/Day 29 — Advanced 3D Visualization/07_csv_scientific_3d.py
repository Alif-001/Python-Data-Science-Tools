import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

"""
CSV SCIENTIFIC 3D VISUALIZATION
------------------------------
Real measured scientific data in 3D space.
"""

x = []
y = []
z = []

# Read CSV
with open("scientific_3d_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x.append(float(row["x"]))
        y.append(float(row["y"]))
        z.append(float(row["z"]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter real data
ax.scatter(x, y, z, c=z, cmap="coolwarm", s=50)

# Connect points (line view)
ax.plot(x, y, z, color="black", alpha=0.5)

ax.set_title("Scientific 3D Data Visualization")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()