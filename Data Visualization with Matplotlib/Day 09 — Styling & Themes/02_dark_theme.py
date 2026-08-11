import matplotlib.pyplot as plt

"""
DARK THEME
----------
Used in modern dashboards and apps.
"""

# Dark background style
plt.style.use("dark_background")

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y, color="cyan", linewidth=2)

plt.title("Dark Theme Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()