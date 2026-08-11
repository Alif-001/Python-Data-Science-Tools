import matplotlib.pyplot as plt
import numpy as np

"""
CLEAN MODERN DASHBOARD STYLE
---------------------------
Minimal professional design
"""

days = np.arange(1, 8)
sales = np.array([100, 120, 150, 130, 170, 180, 200])

fig, axes = plt.subplots(2, 2, figsize=(12, 7))

# Top-left
axes[0, 0].plot(days, sales, color="blue")
axes[0, 0].set_title("Sales Trend")

# Top-right
axes[0, 1].bar(days, sales, color="orange")
axes[0, 1].set_title("Sales Bar")

# Bottom-left
axes[1, 0].hist(sales, bins=5, color="green")
axes[1, 0].set_title("Distribution")

# Bottom-right
axes[1, 1].plot(days, sales ** 1.1, color="purple")
axes[1, 1].set_title("Growth Curve")

plt.tight_layout()

plt.show()