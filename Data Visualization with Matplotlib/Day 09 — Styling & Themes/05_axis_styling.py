import matplotlib.pyplot as plt

"""
AXIS STYLING
------------
We customize axis appearance.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

# Customize axis labels
plt.xlabel("X Axis", fontsize=12, color="green")
plt.ylabel("Y Axis", fontsize=12, color="blue")

# Change tick colors
plt.tick_params(axis="x", colors="red")
plt.tick_params(axis="y", colors="purple")

plt.title("Axis Styling Example")

plt.show()