import matplotlib.pyplot as plt

"""
ALPHA (TRANSPARENCY)
--------------------
alpha controls how transparent a line is
0 = fully invisible
1 = fully visible
"""

x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 15]

plt.plot(x, y, color="green", alpha=0.4, linewidth=4)

plt.title("Transparency Example (alpha)")
plt.show()