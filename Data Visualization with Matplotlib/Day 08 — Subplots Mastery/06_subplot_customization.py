import matplotlib.pyplot as plt

"""
SUBPLOT CUSTOMIZATION
---------------------
We style each subplot differently.
"""

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# First plot
ax[0].plot(x, y, color="blue", marker="o")
ax[0].set_title("Styled Plot 1")
ax[0].grid(True)

# Second plot
ax[1].bar(x, y, color="orange")
ax[1].set_title("Styled Bar Plot")
ax[1].grid(True)

plt.tight_layout()
plt.show()