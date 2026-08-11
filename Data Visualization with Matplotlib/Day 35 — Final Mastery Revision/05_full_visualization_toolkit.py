import matplotlib.pyplot as plt
import numpy as np

"""
FULL TOOLKIT RECAP
------------------
All major plot types in one file.
"""

x = np.linspace(0, 10, 50)

plt.figure(figsize=(12, 8))

# Line plot
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
plt.title("Line Plot")

# Scatter plot
plt.subplot(2, 2, 2)
plt.scatter(x, np.cos(x))
plt.title("Scatter Plot")

# Bar plot
plt.subplot(2, 2, 3)
plt.bar(range(10), np.random.randint(1, 10, 10))
plt.title("Bar Plot")

# Histogram
plt.subplot(2, 2, 4)
plt.hist(np.random.randn(100))
plt.title("Histogram")

plt.tight_layout()
plt.show()