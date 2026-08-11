import matplotlib.pyplot as plt
import numpy as np

"""
STANDARD DEVIATION IDEA
-----------------------
Shows spread of data around mean.
"""

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

# Calculate standard deviation
std = np.std(y)

# Same error for all points (simplified example)
plt.errorbar(x, y, yerr=std, fmt='o', capsize=5)

plt.title("Standard Deviation Error Bars")

plt.show()