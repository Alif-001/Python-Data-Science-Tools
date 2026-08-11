import matplotlib.pyplot as plt
import csv
import numpy as np

"""
REAL DATASET + COLORMAP
----------------------
We visualize temperature using heatmap style.
"""

cities = []
data = []

# Read CSV file
with open("temperature_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cities.append(row["city"])

        data.append([
            int(row["jan"]),
            int(row["feb"]),
            int(row["mar"]),
            int(row["apr"]),
            int(row["may"]),
            int(row["jun"])
        ])

data = np.array(data)

# Heatmap using colormap
plt.imshow(data, cmap="coolwarm")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

plt.xticks(range(len(months)), months)
plt.yticks(range(len(cities)), cities)

plt.title("City Temperature Heatmap with Colormap")
plt.colorbar()

plt.show()