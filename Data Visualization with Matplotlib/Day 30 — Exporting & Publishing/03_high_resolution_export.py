import matplotlib.pyplot as plt
import numpy as np

"""
HIGH RESOLUTION EXPORT
---------------------
DPI = dots per inch (image quality)
Higher DPI = sharper image
"""

x = np.linspace(0, 10, 100)
y = np.sin(x) * np.cos(x)

plt.plot(x, y)

plt.title("High Resolution Export")

# dpi=300 is standard for publication quality
plt.savefig("high_res_plot.png", dpi=300)

plt.show()