import matplotlib.pyplot as plt

"""
BASIC LINE PLOT
---------------
Line plot connects points with a line
It is used to show trends over time
"""

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

plt.plot(x, y)

# Add labels and title (VERY IMPORTANT)
plt.xlabel("X Axis (Input Values)")
plt.ylabel("Y Axis (Output Values)")
plt.title("My First Line Plot")

plt.show()