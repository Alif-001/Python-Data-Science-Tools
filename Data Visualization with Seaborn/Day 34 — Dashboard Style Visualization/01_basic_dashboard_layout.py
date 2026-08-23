# 01_basic_dashboard_layout.py

# --------------------------------------------

# DAY 34: DASHBOARD STYLE VISUALIZATION

# --------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

# --------------------------------------------

# CREATE DASHBOARD LAYOUT

# --------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --------------------------------------------

# PLOT 1: SALES

# --------------------------------------------

sns.lineplot(
data=df,
x="month",
y="sales",
ax=axes[0],
marker="o"
)

axes[0].set_title("Monthly Sales Trend")

# --------------------------------------------

# PLOT 2: PROFIT

# --------------------------------------------

sns.lineplot(
data=df,
x="month",
y="profit",
ax=axes[1],
marker="o"
)

axes[1].set_title("Monthly Profit Trend")

# --------------------------------------------

# FINAL LAYOUT FIX

# --------------------------------------------

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - simple 2-panel dashboard

# --------------------------------------------
