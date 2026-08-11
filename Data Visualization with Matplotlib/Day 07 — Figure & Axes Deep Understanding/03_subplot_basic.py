import matplotlib.pyplot as plt

"""
SUBPLOT
-------
Used to create multiple plots in one figure.
"""

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

# Create 2 rows, 1 column
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.tight_layout()  # prevents overlap

plt.show()