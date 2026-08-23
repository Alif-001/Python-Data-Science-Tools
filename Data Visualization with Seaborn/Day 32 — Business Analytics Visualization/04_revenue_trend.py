# 04_revenue_trend.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

# Convert date

df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# REVENUE TREND

# --------------------------------------------

sns.lineplot(
data=df,
x="date",
y="sales",
marker="o"
)

plt.title("Revenue Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# INSIGHT:

# - growth or decline detection

# --------------------------------------------
