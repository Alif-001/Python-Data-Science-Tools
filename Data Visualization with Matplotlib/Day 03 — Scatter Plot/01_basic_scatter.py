import matplotlib.pyplot as plt

"""
DAY 3 - SCATTER PLOT
--------------------
Scatter plot shows relationship between two variables.
Each point = one data observation.
"""

# X values (independent variable)
x = [1, 2, 3, 4, 5]

# Y values (dependent variable)
y = [2, 4, 6, 8, 10]

# Create scatter plot
plt.scatter(x, y)

plt.title("Basic Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()