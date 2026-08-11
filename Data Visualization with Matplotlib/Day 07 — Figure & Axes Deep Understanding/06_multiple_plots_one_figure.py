import matplotlib.pyplot as plt

"""
MULTIPLE PLOTS IN ONE FIGURE
----------------------------
Using axes object (modern way)
"""

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Plot 1
ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 0].set_title("Plot 1")

# Plot 2
ax[0, 1].plot([1, 2, 3], [2, 4, 6])
ax[0, 1].set_title("Plot 2")

# Plot 3
ax[1, 0].plot([1, 2, 3], [3, 6, 9])
ax[1, 0].set_title("Plot 3")

# Plot 4
ax[1, 1].plot([1, 2, 3], [4, 8, 12])
ax[1, 1].set_title("Plot 4")

plt.tight_layout()

plt.show()