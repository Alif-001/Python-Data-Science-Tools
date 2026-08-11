import matplotlib.pyplot as plt

"""
DAY 2 - Multiple Line Plots
---------------------------
We can draw more than one line in a single graph.
This is useful for comparison (e.g., sales vs profit).
"""

# Data for first line
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Data for second line
y2 = [1, 3, 5, 7, 9]

# First line
plt.plot(x, y1)

# Second line
plt.plot(x, y2)

plt.title("Multiple Line Plot Example")
plt.show()