import matplotlib.pyplot as plt
import numpy as np

"""
LEGEND POSITIONING
------------------
We place legend in different locations.
"""

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), label="Sin")
plt.plot(x, np.cos(x), label="Cos")

# Try different positions:
# "upper left", "upper right", "lower left", "lower right", "center"
plt.legend(loc="lower left")

plt.title("Legend Position Control")
plt.grid(True)

plt.show()