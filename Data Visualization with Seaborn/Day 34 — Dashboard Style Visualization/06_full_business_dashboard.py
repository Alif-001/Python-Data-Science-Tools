# 06_full_business_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

plt.style.use("seaborn-v0_8")

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# SALES TREND

sns.lineplot(data=df, x="month", y="sales", ax=axes[0,0], marker="o")
axes[0,0].set_title("Sales Trend")

# PROFIT TREND

sns.lineplot(data=df, x="month", y="profit", ax=axes[0,1], marker="o")
axes[0,1].set_title("Profit Trend")

# CUSTOMERS

sns.lineplot(data=df, x="month", y="customers", ax=axes[0,2], marker="o")
axes[0,2].set_title("Customer Growth")

# REGION SALES

sns.barplot(data=df, x="region", y="sales", ax=axes[1,0])
axes[1,0].set_title("Region Sales")

# ADS SPEND

sns.lineplot(data=df, x="month", y="ads", ax=axes[1,1], marker="o")
axes[1,1].set_title("Ad Spend Trend")

# PROFIT VS SALES

sns.scatterplot(data=df, x="sales", y="profit", ax=axes[1,2], hue="region")
axes[1,2].set_title("Profit Analysis")

plt.suptitle("FULL BUSINESS DASHBOARD", fontsize=18)

plt.tight_layout()
plt.show()

# --------------------------------------------

# FINAL RESULT:

# - complete business intelligence system

# --------------------------------------------
