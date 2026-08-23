# 04_trend_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# TREND VISUALIZATION WITH REGRESSION STYLE

# --------------------------------------------

sns.regplot(
x=df.index,
y=df["sales"]
)

plt.title("Trend Analysis (Sales Growth)")
plt.xlabel("Time Index")
plt.ylabel("Sales")
plt.show()

# --------------------------------------------

# IDEA:

# - upward trend = growth

# - downward = decline

# --------------------------------------------
