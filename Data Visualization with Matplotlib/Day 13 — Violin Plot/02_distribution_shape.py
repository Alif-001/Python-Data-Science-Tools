import matplotlib.pyplot as plt
import numpy as np

"""
DISTRIBUTION SHAPE
------------------
Violin plot shows the "shape" of data distribution.
"""

# Two different distributions
data1 = np.random.normal(50, 5, 100)
data2 = np.random.normal(70, 15, 100)

plt.violinplot([data1, data2])

plt.title("Distribution Shape Comparison")

plt.show()