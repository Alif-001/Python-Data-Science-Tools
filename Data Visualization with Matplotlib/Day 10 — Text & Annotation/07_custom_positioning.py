import matplotlib.pyplot as plt

"""
CUSTOM POSITIONING
------------------
We control exact placement of text.
"""

x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 15]

plt.plot(x, y, marker="o")

# Different positions
plt.text(1, 3, "Start", fontsize=12)
plt.text(5, 15, "End", fontsize=12)

plt.title("Custom Positioning Example")

plt.show()