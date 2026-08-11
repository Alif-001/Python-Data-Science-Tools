import matplotlib.pyplot as plt
import numpy as np

"""
PORTFOLIO-READY DASHBOARD
-------------------------
This is what you show in interviews / GitHub.
"""

days = np.arange(1, 8)
sales = [100, 120, 150, 130, 170, 180, 200]
profit = [20, 30, 40, 35, 50, 55, 60]

plt.figure(figsize=(12, 6))

# Sales trend
plt.subplot(2, 2, 1)
plt.plot(days, sales, marker="o", color="blue")
plt.title("Sales Trend")

# Profit trend
plt.subplot(2, 2, 2)
plt.plot(days, profit, marker="o", color="green")
plt.title("Profit Trend")

# Comparison
plt.subplot(2, 2, 3)
plt.bar(days, sales, label="Sales")
plt.bar(days, profit, label="Profit", alpha=0.7)
plt.title("Comparison")

# Growth curve
plt.subplot(2, 2, 4)
plt.plot(days, np.array(sales) * 1.1)
plt.title("Growth Projection")

plt.tight_layout()
plt.show()