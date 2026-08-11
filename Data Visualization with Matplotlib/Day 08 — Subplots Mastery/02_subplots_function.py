import matplotlib.pyplot as plt

"""
plt.subplots() - MODERN WAY
---------------------------
More flexible than plt.subplot()
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

# Create figure + axes
fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, y)
ax[0, 0].set_title("Plot 1")

ax[0, 1].plot(y, x)
ax[0, 1].set_title("Plot 2")

ax[1, 0].plot(x, [i*2 for i in x])
ax[1, 0].set_title("Plot 3")

ax[1, 1].plot(y, [i/2 for i in y])
ax[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.show()