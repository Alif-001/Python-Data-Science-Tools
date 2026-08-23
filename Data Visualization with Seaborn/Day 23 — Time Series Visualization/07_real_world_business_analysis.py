# 07_real_world_business_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# BUSINESS ANALYSIS VIEW

# --------------------------------------------

df["sales_roll"] = df["sales"].rolling(window=3).mean()

sns.lineplot(data=df, x="date", y="sales", label="Sales")
sns.lineplot(data=df, x="date", y="sales_roll", label="Trend (Rolling Avg)")

plt.title("Business Sales Trend Analysis")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# INSIGHT:

# - real decision-making tool

# --------------------------------------------
