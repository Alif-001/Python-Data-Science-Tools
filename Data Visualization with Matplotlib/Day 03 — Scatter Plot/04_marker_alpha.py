import matplotlib.pyplot as plt

"""
MARKER + ALPHA
--------------
marker = shape of points
alpha = transparency
"""

x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 15]

plt.scatter(
    x, y,
    marker="o",   # circle shape
    alpha=0.5,    # transparency
    s=200
)

plt.title("Marker and Transparency Example")
plt.show()