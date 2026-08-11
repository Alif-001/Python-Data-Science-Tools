import numpy as np
import matplotlib.pyplot as plt

"""
BOX PLOT (STATISTICS VISUALIZATION)
-----------------------------------
Shows:
- median
- quartiles
- outliers
"""

data = np.random.randint(10, 100, 50)

plt.boxplot(data)

plt.title("Box Plot Visualization")
plt.ylabel("Values")

plt.grid(True)

plt.show()