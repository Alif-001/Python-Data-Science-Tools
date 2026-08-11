import matplotlib.pyplot as plt

"""
HIGHLIGHT POINTS
----------------
We highlight important values using different colors.
"""

x = [1, 2, 3, 4, 5]
y = [5, 15, 10, 25, 20]

plt.plot(x, y, color="blue")

# Highlight max value manually
plt.scatter([4], [25], color="red", s=100)

plt.text(4, 25, "Max Value", fontsize=12, color="red")

plt.title("Highlight Important Point")

plt.show()