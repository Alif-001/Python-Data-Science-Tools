import matplotlib.pyplot as plt
import numpy as np

"""
KPI + CHART COMBINATION DASHBOARD
--------------------------------
Mix of text KPIs + charts
"""

days = np.arange(1, 8)
sales = np.array([100, 120, 150, 130, 170, 180, 200])

plt.figure(figsize=(12, 6))

# ---- KPI Panel ----
plt.subplot(1, 2, 1)

total_sales = np.sum(sales)
avg_sales = np.mean(sales)

plt.text(0.1, 0.7, f"Total Sales: {total_sales}", fontsize=14)
plt.text(0.1, 0.5, f"Average Sales: {avg_sales:.2f}", fontsize=14)

plt.title("KPI Panel")
plt.axis("off")

# ---- Chart Panel ----
plt.subplot(1, 2, 2)
plt.plot(days, sales, marker="o")
plt.title("Sales Trend")

plt.tight_layout()

plt.show()