import matplotlib.pyplot as plt

"""
CUSTOM TICKS
------------
We can control what numbers appear on axis.
"""

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

# Custom x-axis ticks
plt.xticks([1, 2, 3, 4, 5], ["A", "B", "C", "D", "E"])

# Custom y-axis ticks
plt.yticks([10, 20, 30, 40, 50])

plt.title("Custom Axis Labels")
plt.show()