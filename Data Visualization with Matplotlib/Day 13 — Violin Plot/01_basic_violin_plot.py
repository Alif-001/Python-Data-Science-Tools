import matplotlib.pyplot as plt
import numpy as np

"""
DAY 13 - VIOLIN PLOT
--------------------
Violin plot shows:
- Data distribution
- Density (where data is concentrated)
- Similar to box plot but more detailed shape
"""

# Sample data
data = np.random.normal(50, 10, 100)  # mean=50, std=10

# Create violin plot
plt.violinplot(data)

plt.title("Basic Violin Plot")

plt.show()