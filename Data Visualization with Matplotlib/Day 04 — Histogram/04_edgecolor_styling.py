import matplotlib.pyplot as plt

"""
EDGE COLOR + STYLING
--------------------
edgecolor = border of bars
"""

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
         95, 40, 42, 47, 53, 58, 62, 68, 72, 78]

plt.hist(
    marks,
    bins=6,
    color="orange",
    edgecolor="black"  # makes bars visible clearly
)

plt.title("Histogram with Edge Color")
plt.show()