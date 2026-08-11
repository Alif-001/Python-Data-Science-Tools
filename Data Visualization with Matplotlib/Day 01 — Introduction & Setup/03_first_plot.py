# Import pyplot module from matplotlib
# pyplot is the most commonly used part of matplotlib
import matplotlib.pyplot as plt

"""
FIRST SIMPLE PLOT
------------------
We will plot a simple graph using some numbers
"""

# X-axis values
x = [1, 2, 3, 4, 5]

# Y-axis values
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y)

# Show the plot window
plt.show()