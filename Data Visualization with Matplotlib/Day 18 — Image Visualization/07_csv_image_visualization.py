import matplotlib.pyplot as plt
import numpy as np
import csv

"""
CSV IMAGE VISUALIZATION
-----------------------
We treat CSV as pixel values (like an image).
"""

data = []

# Read CSV file
with open("pixel_data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        data.append([int(x) for x in row])

data = np.array(data)

plt.imshow(data, cmap="gray")

plt.title("Image from CSV Data")

plt.colorbar()

plt.show()