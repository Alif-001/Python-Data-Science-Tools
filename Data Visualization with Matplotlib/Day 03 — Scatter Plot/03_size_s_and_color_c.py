import matplotlib.pyplot as plt

"""
SIZE (s) AND COLOR (c)
----------------------
s = size of points
c = color of points
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Size of each point
sizes = [50, 100, 200, 300, 400]

# Color of each point
colors = [10, 20, 30, 40, 50]

plt.scatter(
    x, y,
    s=sizes,      # size of dots
    c=colors,     # color intensity
    cmap="viridis"  # color map style
)

plt.title("Scatter with Size and Color")
plt.colorbar(label="Color Scale")

plt.show()