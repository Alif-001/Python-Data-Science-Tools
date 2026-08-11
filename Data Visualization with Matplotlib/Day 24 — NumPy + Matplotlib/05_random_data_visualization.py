import numpy as np
import matplotlib.pyplot as plt

"""
RANDOM DATA VISUALIZATION
-------------------------
Used in:
- machine learning
- simulation
- noise analysis
"""

# Generate random values
x = np.arange(0, 50)
y = np.random.randn(50)  # random normal distribution

plt.plot(x, y, marker="o")

plt.title("Random Data Visualization")
plt.xlabel("Index")
plt.ylabel("Value")

plt.grid(True)

plt.show()