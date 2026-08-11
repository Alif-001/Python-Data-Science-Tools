import numpy as np
import matplotlib.pyplot as plt

"""
DISTRIBUTION COMPARISON
----------------------
Compare two datasets (e.g. two classes, A/B test)
"""

# Dataset A
data_a = np.random.normal(50, 10, 100)

# Dataset B
data_b = np.random.normal(60, 15, 100)

plt.hist(data_a, alpha=0.5, label="Group A")
plt.hist(data_b, alpha=0.5, label="Group B")

plt.title("Distribution Comparison")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.legend()
plt.grid(True)

plt.show()