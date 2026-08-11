import matplotlib.pyplot as plt

"""
ROW / COLUMN LAYOUT
-------------------
We arrange plots in rows and columns.
"""

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

fig, ax = plt.subplots(3, 1, figsize=(5, 8))  # 3 rows, 1 column

ax[0].plot(x, y)
ax[0].set_title("Plot 1")

ax[1].plot(y, x)
ax[1].set_title("Plot 2")

ax[2].plot(x, [i**2 for i in x])
ax[2].set_title("Plot 3")

plt.tight_layout()
plt.show()