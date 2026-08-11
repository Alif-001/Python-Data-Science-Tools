import matplotlib.pyplot as plt

"""
TIGHT LAYOUT
------------
Automatically adjusts spacing between plots.
Prevents overlap.
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots(2, 1)

ax[0].plot(x, y)
ax[0].set_title("Top Plot")

ax[1].plot(y, x)
ax[1].set_title("Bottom Plot")

# IMPORTANT: fixes overlapping text
plt.tight_layout()

plt.show()