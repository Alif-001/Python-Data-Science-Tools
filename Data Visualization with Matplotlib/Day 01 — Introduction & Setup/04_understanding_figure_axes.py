import matplotlib.pyplot as plt

"""
UNDERSTANDING FIGURE & AXES

Figure = Whole canvas (like a page)
Axes   = Actual graph area inside figure
"""

# Create figure and axes manually
fig, ax = plt.subplots()

# ax is where we draw the graph
ax.plot([1, 2, 3], [1, 4, 9])

# Show plot
plt.show()