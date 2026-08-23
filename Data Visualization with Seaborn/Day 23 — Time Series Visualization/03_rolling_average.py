# 03_rolling_average.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# ROLLING AVERAGE (SMOOTH TREND)

# --------------------------------------------

df["sales_roll"] = df["sales"].rolling(window=3).mean()

# --------------------------------------------

# PLOT ORIGINAL + SMOOTHED LINE

# --------------------------------------------

sns.lineplot(data=df, x="date", y="sales", label="Original Sales")
sns.lineplot(data=df, x="date", y="sales_roll", label="Rolling Avg")

plt.title("Sales Trend (Smoothed)")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# IDEA:

# - removes noise

# - shows real trend

# --------------------------------------------
