import matplotlib.pyplot as plt

"""
LINETYPE + MARKER
------------------
linestyle = how line looks
marker = points style on graph
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(
    x, y,
    color="blue",        # line color
    linestyle="--",      # dashed line
    marker="o",          # circle marker on points
    markersize=8         # size of marker
)

plt.title("Line Style + Marker Example")
plt.show()