import matplotlib.pyplot as plt
import numpy as np

"""
STEP PLOT BASICS
----------------
Step plot = values change suddenly (not smooth).
Used for:
- stock price changes
- system states
"""

x = np.arange(0, 10)
y = np.array([1, 2, 2, 3, 5, 5, 6, 7, 7, 8])

plt.step(x, y, where="mid")

plt.title("Basic Step Plot")
plt.xlabel("Time")
plt.ylabel("Value")

plt.show()