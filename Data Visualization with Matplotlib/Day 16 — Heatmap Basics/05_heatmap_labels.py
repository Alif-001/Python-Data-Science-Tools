import matplotlib.pyplot as plt
import numpy as np

"""
HEATMAP WITH LABELS
-------------------
We add readable labels to rows and columns.
"""

data = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 95]
])

subjects = ["Math", "Science", "English"]
students = ["A", "B", "C"]

plt.imshow(data, cmap="coolwarm")

# Set labels
plt.xticks(range(len(subjects)), subjects)
plt.yticks(range(len(students)), students)

plt.title("Student Score Heatmap")
plt.colorbar()

plt.show()