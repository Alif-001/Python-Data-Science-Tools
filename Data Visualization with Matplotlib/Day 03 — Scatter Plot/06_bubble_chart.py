import matplotlib.pyplot as plt

"""
BUBBLE CHART
------------
Scatter plot where:
- x = value
- y = value
- size = importance / weight
"""

x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 11, 13]

# Bigger value = bigger bubble
sizes = [100, 200, 300, 400, 500]

plt.scatter(x, y, s=sizes, alpha=0.5, color="green")

plt.title("Bubble Chart Example")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()