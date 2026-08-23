# 03_storytelling_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

# --------------------------------------------

# STORY 1: SALES TREND

# --------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.lineplot(data=df, x="month", y="sales", ax=axes[0,0], marker="o")
axes[0,0].set_title("Sales Growth Over Time")

# --------------------------------------------

# STORY 2: PROFIT TREND

# --------------------------------------------

sns.lineplot(data=df, x="month", y="profit", ax=axes[0,1], marker="o")
axes[0,1].set_title("Profit Growth Over Time")

# --------------------------------------------

# STORY 3: REGION PERFORMANCE

# --------------------------------------------

sns.barplot(data=df, x="region", y="sales", ax=axes[1,0])
axes[1,0].set_title("Regional Sales Performance")

# --------------------------------------------

# STORY 4: CUSTOMER GROWTH

# --------------------------------------------

sns.lineplot(data=df, x="month", y="customers", ax=axes[1,1], marker="o")
axes[1,1].set_title("Customer Growth Trend")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - data storytelling in one view

# --------------------------------------------
