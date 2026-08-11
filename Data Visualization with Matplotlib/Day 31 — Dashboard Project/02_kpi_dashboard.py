import matplotlib.pyplot as plt
import numpy as np

"""
KPI DASHBOARD
------------
KPI = Key Performance Indicator
Example: Total sales, average profit, growth rate
"""

sales = np.array([100, 120, 150, 130, 170, 180, 200])
profit = np.array([20, 30, 40, 35, 50, 55, 60])

# KPI calculations
total_sales = np.sum(sales)
avg_profit = np.mean(profit)
max_sales = np.max(sales)

plt.figure(figsize=(10, 5))

# KPI TEXT BOXES
plt.text(0.1, 0.8, f"Total Sales: {total_sales}", fontsize=12)
plt.text(0.1, 0.6, f"Average Profit: {avg_profit:.2f}", fontsize=12)
plt.text(0.1, 0.4, f"Max Sales: {max_sales}", fontsize=12)

plt.title("KPI Dashboard (Text-Based)")

# Hide axes (dashboard style)
plt.axis("off")

plt.show()