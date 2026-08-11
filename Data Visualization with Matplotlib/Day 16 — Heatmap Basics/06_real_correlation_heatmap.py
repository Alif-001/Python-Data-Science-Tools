import matplotlib.pyplot as plt
import csv
import numpy as np

"""
REAL CORRELATION HEATMAP
------------------------
We calculate correlation manually from dataset.
"""

math = []
science = []
english = []

# Read CSV file
with open("student_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math.append(int(row["math"]))
        science.append(int(row["science"]))
        english.append(int(row["english"]))

# Convert to matrix form
data = np.array([math, science, english])

# Correlation matrix
corr_matrix = np.corrcoef(data)

plt.imshow(corr_matrix, cmap="coolwarm")
plt.colorbar()

subjects = ["Math", "Science", "English"]

plt.xticks(range(3), subjects)
plt.yticks(range(3), subjects)

plt.title("Real Correlation Heatmap")

plt.show()