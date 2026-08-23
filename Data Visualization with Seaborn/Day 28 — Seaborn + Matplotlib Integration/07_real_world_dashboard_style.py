# 07_real_world_dashboard_style.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("performance.csv")

# --------------------------------------------

# DASHBOARD STYLE FIGURE

# --------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# SALES

sns.barplot(data=df, x="team", y="sales", ax=axes[0])
axes[0].set_title("Team Sales")

# PROFIT

sns.barplot(data=df, x="team", y="profit", ax=axes[1])
axes[1].set_title("Team Profit")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - real business dashboard layout

# --------------------------------------------
