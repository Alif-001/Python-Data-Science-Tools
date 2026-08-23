# 04_advanced_dashboard_style.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

# --------------------------------------------

# PROFESSIONAL DASHBOARD STYLE

# --------------------------------------------

plt.style.use("ggplot")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# SALES

sns.lineplot(data=df, x="month", y="sales", ax=axes[0,0])
axes[0,0].set_title("Sales Trend")

# PROFIT

sns.lineplot(data=df, x="month", y="profit", ax=axes[0,1])
axes[0,1].set_title("Profit Trend")

# REGION SALES

sns.barplot(data=df, x="region", y="sales", ax=axes[1,0])
axes[1,0].set_title("Region Sales")

# CUSTOMERS

sns.barplot(data=df, x="region", y="customers", ax=axes[1,1])
axes[1,1].set_title("Customers by Region")

plt.suptitle("Business Performance Dashboard", fontsize=16)

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - clean + professional layout

# --------------------------------------------
