# 06_kpi_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# --------------------------------------------

# KPI 1: SALES

# --------------------------------------------

sns.barplot(data=df, x="region", y="sales", ax=axes[0])
axes[0].set_title("Sales KPI")

# --------------------------------------------

# KPI 2: PROFIT

# --------------------------------------------

sns.barplot(data=df, x="region", y="profit", ax=axes[1])
axes[1].set_title("Profit KPI")

# --------------------------------------------

# KPI 3: ORDERS

# --------------------------------------------

sns.barplot(data=df, x="region", y="orders", ax=axes[2])
axes[2].set_title("Orders KPI")

plt.tight_layout()
plt.show()

# --------------------------------------------

# INSIGHT:

# - full business performance snapshot

# --------------------------------------------
