import matplotlib.pyplot as plt
import numpy as np

"""
DAY 31 - DASHBOARD PROJECT
-------------------------
A dashboard = multiple charts in one figure.
Used in:
- business reports
- ML monitoring
- analytics tools
"""

# Sample data
days = np.arange(1, 8)
sales = [100, 120, 150, 130, 170, 180, 200]
profit = [20, 30, 40, 35, 50, 55, 60]

plt.figure(figsize=(10, 6))

# ---- Chart 1 ----
plt.subplot(2, 2, 1)
plt.plot(days, sales, marker="o")
plt.title("Sales Trend")

# ---- Chart 2 ----
plt.subplot(2, 2, 2)
plt.plot(days, profit, marker="o", color="green")
plt.title("Profit Trend")

# ---- Chart 3 ----
plt.subplot(2, 2, 3)
plt.bar(days, sales, color="blue")
plt.title("Sales Bar")

# ---- Chart 4 ----
plt.subplot(2, 2, 4)
plt.bar(days, profit, color="orange")
plt.title("Profit Bar")

plt.tight_layout()

plt.show()