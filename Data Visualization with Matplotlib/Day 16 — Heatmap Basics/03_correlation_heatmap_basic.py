import matplotlib.pyplot as plt
import numpy as np

"""
CORRELATION HEATMAP (BASIC)
---------------------------
Shows relationship between variables.
"""

# Example correlation matrix
corr = np.array([
    [1.0, 0.8, 0.3],
    [0.8, 1.0, 0.5],
    [0.3, 0.5, 1.0]
])

plt.imshow(corr, cmap="coolwarm")
plt.colorbar()

plt.title("Correlation Heatmap (Basic)")

plt.show()