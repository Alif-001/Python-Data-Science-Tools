import matplotlib.pyplot as plt
import numpy as np

"""
SCIENTIFIC PLOTTING
-------------------
Used in research papers and experiments.
"""

x = np.linspace(1, 5, 5)

y = np.array([2.1, 2.5, 3.0, 3.6, 4.2])

# Simulated measurement uncertainty
error = np.array([0.1, 0.2, 0.15, 0.25, 0.3])

plt.errorbar(x, y, yerr=error, fmt='o-', capsize=4)

plt.title("Scientific Experiment Plot")
plt.xlabel("Experiment Step")
plt.ylabel("Measurement")

plt.show()