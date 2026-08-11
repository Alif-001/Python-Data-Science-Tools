import matplotlib.pyplot as plt

"""
STACK PLOT
----------
Used to show contribution of multiple categories over time.
"""

x = [1, 2, 3, 4, 5]

y1 = [2, 3, 4, 5, 6]
y2 = [1, 2, 1, 2, 1]
y3 = [3, 1, 2, 3, 2]

# Stack plot
plt.stackplot(x, y1, y2, y3, labels=["A", "B", "C"], alpha=0.7)

plt.title("Stack Plot Example")
plt.legend()

plt.show()