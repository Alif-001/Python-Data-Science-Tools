import matplotlib.pyplot as plt

"""
SPINE CUSTOMIZATION
-------------------
Spines = border lines around graph
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots()

ax.plot(x, y)

# Remove top and right border
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Change left and bottom color
ax.spines["left"].set_color("red")
ax.spines["bottom"].set_color("blue")

plt.title("Spine Customization Example")

plt.show()