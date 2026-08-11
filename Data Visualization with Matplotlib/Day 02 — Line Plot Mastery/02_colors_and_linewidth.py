import matplotlib.pyplot as plt

"""
COLOR + LINE WIDTH
------------------
We can customize appearance of lines.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# color = line color
# linewidth = thickness of line
plt.plot(x, y, color="red", linewidth=3)

plt.title("Color and Linewidth Example")
plt.show()