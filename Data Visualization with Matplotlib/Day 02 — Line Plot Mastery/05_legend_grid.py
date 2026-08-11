import matplotlib.pyplot as plt

"""
LEGEND + GRID
-------------
legend = identifies lines
grid = adds background grid
"""

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Line A", color="blue")
plt.plot(x, y2, label="Line B", color="red")

# Show legend (VERY IMPORTANT for multiple lines)
plt.legend()

# Add grid background
plt.grid(True)

plt.title("Legend and Grid Example")
plt.show()