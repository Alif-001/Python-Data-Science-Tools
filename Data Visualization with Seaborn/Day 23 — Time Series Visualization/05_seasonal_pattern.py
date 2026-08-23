# 05_seasonal_pattern.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# SEASONAL STYLE VISUALIZATION

# --------------------------------------------

df["day"] = df["date"].dt.day

sns.lineplot(
data=df,
x="day",
y="sales"
)

plt.title("Seasonal Pattern (Daily Variation)")
plt.show()

# --------------------------------------------

# IDEA:

# - detect repeating patterns

# --------------------------------------------
