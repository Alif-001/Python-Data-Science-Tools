import matplotlib.pyplot as plt
import numpy as np

"""
FIGURE LAYOUT CONTROL
--------------------
We control size and spacing of plots.
"""

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 5))  # width, height

plt.plot(x, np.sin(x), label="Sin")
plt.plot(x, np.cos(x), label="Cos")

plt.legend()

plt.title("Figure Size Control")
plt.grid(True)

plt.show()