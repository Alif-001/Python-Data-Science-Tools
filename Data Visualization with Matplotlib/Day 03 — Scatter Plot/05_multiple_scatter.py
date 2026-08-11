import matplotlib.pyplot as plt

"""
MULTIPLE SCATTER PLOTS
----------------------
We can compare different datasets in same graph.
"""

# Dataset 1
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Dataset 2
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

plt.scatter(x1, y1, color="blue", label="Group A")
plt.scatter(x2, y2, color="red", label="Group B")

plt.title("Multiple Scatter Plot")
plt.legend()
plt.show()