import pandas as pd
import matplotlib.pyplot as plt

"""
KPI DASHBOARD (KEY BUSINESS METRICS)
------------------------------------
Real business KPI summary
"""

df = pd.read_csv("business_data.csv")

total_sales = df["sales"].sum()
total_revenue = df["revenue"].sum()
total_customers = df["customers"].sum()
total_returns = df["returns"].sum()

plt.figure(figsize=(8, 5))

plt.text(0.1, 0.8, f"Total Sales: {total_sales}", fontsize=12)
plt.text(0.1, 0.6, f"Total Revenue: {total_revenue}", fontsize=12)
plt.text(0.1, 0.4, f"Total Customers: {total_customers}", fontsize=12)
plt.text(0.1, 0.2, f"Total Returns: {total_returns}", fontsize=12)

plt.title("Business KPI Dashboard")
plt.axis("off")

plt.show()