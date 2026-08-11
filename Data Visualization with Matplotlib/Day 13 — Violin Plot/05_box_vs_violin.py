import matplotlib.pyplot as plt
import numpy as np

"""
BOX PLOT VS VIOLIN PLOT
-----------------------
Box plot = summary
Violin plot = detailed shape
"""

data = np.random.normal(50, 10, 100)

plt.figure(figsize=(8, 4))

# Box plot
plt.subplot(1, 2, 1)
plt.boxplot(data)
plt.title("Box Plot")

# Violin plot
plt.subplot(1, 2, 2)
plt.violinplot(data)
plt.title("Violin Plot")

plt.tight_layout()
plt.show()