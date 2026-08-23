# 07_portfolio_ready_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# SALES

sns.lineplot(data=df, x="month", y="sales", ax=axes[0,0], marker="o")
axes[0,0].set_title("Sales Trend")

# PROFIT

sns.lineplot(data=df, x="month", y="profit", ax=axes[0,1], marker="o")
axes[0,1].set_title("Profit Trend")

# REGION PERFORMANCE

sns.barplot(data=df, x="region", y="sales", ax=axes[1,0])
axes[1,0].set_title("Regional Performance")

# CUSTOMER GROWTH

sns.lineplot(data=df, x="month", y="customers", ax=axes[1,1], marker="o")
axes[1,1].set_title("Customer Growth")

plt.suptitle("Business Analytics Dashboard", fontsize=16)
plt.tight_layout()
plt.show()

# --------------------------------------------

# GOAL:

# - clean, readable, portfolio-ready dashboard

# --------------------------------------------
