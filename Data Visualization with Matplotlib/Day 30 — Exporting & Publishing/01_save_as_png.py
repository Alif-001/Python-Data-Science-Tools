import matplotlib.pyplot as plt
import numpy as np

"""
DAY 30 - EXPORTING & PUBLISHING
------------------------------
We learn how to save plots as image files.
"""

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

plt.title("Save as PNG Example")
plt.xlabel("X")
plt.ylabel("Y")

# IMPORTANT: Save figure BEFORE plt.show()
plt.savefig("plot_basic.png")

plt.show()