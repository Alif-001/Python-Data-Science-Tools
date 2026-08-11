import matplotlib.pyplot as plt

"""
AREA VS LINE
------------
Comparison of visual styles.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 4))

# Line plot
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

# Area plot
plt.subplot(1, 2, 2)
plt.fill_between(x, y, color="green", alpha=0.5)
plt.plot(x, y)
plt.title("Area Plot")

plt.tight_layout()
plt.show()