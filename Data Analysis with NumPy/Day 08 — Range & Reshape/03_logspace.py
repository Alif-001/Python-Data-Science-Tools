import numpy as np

# =========================
# np.logspace → exponential / logarithmic scale data
# =========================

# start power, end power, number of points
arr = np.logspace(1, 3, 5)

print("Logspace Array:", arr)

# base 2 example
arr2 = np.logspace(0, 4, 5, base=2)

print("\nBase 2 Logspace:", arr2)

# ML/AI use case:
# learning rate decay, exponential growth models