import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

"""
CSV BASED 3D SCATTER PLOT
-------------------------
Real data visualization in 3D space.
"""

x = []
y = []
z = []

# Read CSV file
with open("3d_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        x.append(int(row["x"]))
        y.append(int(row["y"]))
        z.append(int(row["z"]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=z, cmap="plasma")

ax.set_title("3D Scatter from CSV")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()