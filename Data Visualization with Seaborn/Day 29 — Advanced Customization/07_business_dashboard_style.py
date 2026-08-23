# 07_business_dashboard_style.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("marketing.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ADS vs SALES

sns.lineplot(data=df, x="month", y="ads", ax=axes[0], marker="o")
axes[0].set_title("Ad Spend Over Time")

# SALES TREND

sns.lineplot(data=df, x="month", y="sales", ax=axes[1], marker="o")
axes[1].set_title("Sales Growth Over Time")

plt.suptitle("Marketing Performance Dashboard", fontsize=14)

plt.tight_layout()

plt.show()

# --------------------------------------------

# IDEA:

# - real business dashboard style

# --------------------------------------------
