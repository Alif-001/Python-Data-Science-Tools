# 08_final_business_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# SALES TREND

sns.lineplot(data=df, x="date", y="sales", ax=axes[0,0])
axes[0,0].set_title("Sales Trend")

# REGION SALES

sns.barplot(data=df, x="region", y="sales", ax=axes[0,1])
axes[0,1].set_title("Region Sales")

# CUSTOMER SEGMENT

sns.barplot(data=df, x="customer_type", y="sales", ax=axes[1,0])
axes[1,0].set_title("Customer Segmentation")

# PROFIT RELATIONSHIP

sns.scatterplot(data=df, x="sales", y="profit", ax=axes[1,1])
axes[1,1].set_title("Profit Analysis")

plt.tight_layout()
plt.show()

# --------------------------------------------

# FINAL RESULT:

# - full business intelligence dashboard

# --------------------------------------------
