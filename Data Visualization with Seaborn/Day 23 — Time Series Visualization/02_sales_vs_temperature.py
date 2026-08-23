# 02_sales_vs_temperature.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# MULTI-LINE TIME SERIES

# --------------------------------------------

sns.lineplot(
data=df,
x="date",
y="sales",
label="Sales"
)

sns.lineplot(
data=df,
x="date",
y="temperature",
label="Temperature"
)

plt.title("Sales vs Temperature Over Time")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# IDEA:

# - compare 2 time-based variables

# --------------------------------------------
