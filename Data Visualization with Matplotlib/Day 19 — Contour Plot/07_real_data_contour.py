import numpy as np
import matplotlib.pyplot as plt
import csv

"""
REAL DATA CONTOUR PLOT
----------------------
We visualize real grid data (like temperature map).
"""

data = []

# Read CSV
with open("temperature_grid.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        data.append([int(x) for x in row])

Z = np.array(data)

# Create X and Y coordinates
x = np.arange(Z.shape[1])
y = np.arange(Z.shape[0])

X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, Z, cmap="coolwarm")

plt.title("Real Temperature Contour Map")
plt.colorbar()

plt.show()