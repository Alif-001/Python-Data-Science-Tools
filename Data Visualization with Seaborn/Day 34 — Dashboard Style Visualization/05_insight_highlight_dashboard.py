# 05_insight_highlight_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard_data.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# SALES vs PROFIT RELATION

sns.scatterplot(
data=df,
x="sales",
y="profit",
hue="region",
ax=axes[0]
)

axes[0].set_title("Sales vs Profit Insight")

# CUSTOMER GROWTH

sns.lineplot(
data=df,
x="month",
y="customers",
ax=axes[1],
marker="o"
)

axes[1].set_title("Customer Growth Trend")

# --------------------------------------------

# INSIGHT ANNOTATION

# --------------------------------------------

axes[1].text(3, 80, "Fast Growth Period", color="red")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - highlight business insight visually

# --------------------------------------------
