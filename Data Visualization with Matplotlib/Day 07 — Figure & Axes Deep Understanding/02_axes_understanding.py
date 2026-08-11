import matplotlib.pyplot as plt

"""
AXES UNDERSTANDING
-------------------
Axes = Actual plotting area inside the figure.
"""

# Create figure + axes manually
fig = plt.figure()

# Add axes: [left, bottom, width, height]
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Data
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# Plot on axes
ax.plot(x, y)

ax.set_title("Axes Example")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

plt.show()