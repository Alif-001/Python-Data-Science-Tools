import matplotlib.pyplot as plt
import numpy as np

"""
SEQUENTIAL COLORMAP
-------------------
Used when values go from LOW → HIGH
Example:
- temperature
- sales
- marks
"""

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Blue gradient (light → dark)
plt.imshow(data, cmap="Blues")

plt.title("Sequential Colormap (Blues)")
plt.colorbar()

plt.show()