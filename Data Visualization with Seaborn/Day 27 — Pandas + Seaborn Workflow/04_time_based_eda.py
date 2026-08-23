# 04_time_based_eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_eda.csv")

# Convert date

df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# TIME SERIES EDA

# --------------------------------------------

sns.lineplot(
data=df,
x="date",
y="sales",
marker="o"
)

plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# IDEA:

# - detect trend over time

# --------------------------------------------
