import matplotlib.pyplot as plt
import numpy as np

"""
GROUPED BAR CHART
-----------------
Used to compare multiple groups side by side.
Example: Boys vs Girls marks
"""

subjects = ["Math", "English", "Science"]

boys = [70, 80, 90]
girls = [75, 85, 95]

# Position of bars
x = np.arange(len(subjects))

# Bar width
width = 0.35

plt.bar(x - width/2, boys, width, label="Boys", color="blue")
plt.bar(x + width/2, girls, width, label="Girls", color="pink")

plt.xticks(x, subjects)

plt.title("Grouped Bar Chart")
plt.legend()

plt.show()