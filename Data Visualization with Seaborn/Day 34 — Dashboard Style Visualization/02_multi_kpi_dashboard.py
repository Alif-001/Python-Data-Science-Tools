# 02_multi_kpi_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

# --------------------------------------------

# MULTI KPI DASHBOARD

# --------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# SALES KPI

sns.barplot(data=df, x="region", y="sales", ax=axes[0])
axes[0].set_title("Sales KPI")

# PROFIT KPI

sns.barplot(data=df, x="region", y="profit", ax=axes[1])
axes[1].set_title("Profit KPI")

# CUSTOMERS KPI

sns.barplot(data=df, x="region", y="customers", ax=axes[2])
axes[2].set_title("Customers KPI")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - business performance comparison

# --------------------------------------------
