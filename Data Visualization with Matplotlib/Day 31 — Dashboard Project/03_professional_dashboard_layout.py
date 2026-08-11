import matplotlib.pyplot as plt
import numpy as np

"""
PROFESSIONAL DASHBOARD LAYOUT
----------------------------
Clean layout used in real analytics dashboards.
"""

days = np.arange(1, 8)
sales = np.array([100, 120, 150, 130, 170, 180, 200])
profit = np.array([20, 30, 40, 35, 50, 55, 60])

plt.figure(figsize=(12, 7))

# ---- Sales Line ----
ax1 = plt.subplot(2, 2, 1)
ax1.plot(days, sales, color="blue")
ax1.set_title("Sales Trend")

# ---- Profit Line ----
ax2 = plt.subplot(2, 2, 2)
ax2.plot(days, profit, color="green")
ax2.set_title("Profit Trend")

# ---- Sales Bar ----
ax3 = plt.subplot(2, 2, 3)
ax3.bar(days, sales, color="skyblue")
ax3.set_title("Sales Bar Chart")

# ---- Profit Bar ----
ax4 = plt.subplot(2, 2, 4)
ax4.bar(days, profit, color="lightgreen")
ax4.set_title("Profit Bar Chart")

plt.tight_layout()

plt.show()