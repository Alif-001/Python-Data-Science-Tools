# 06_multi_variable_time_series.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# MULTI VARIABLE TIME SERIES

# --------------------------------------------

sns.lineplot(data=df, x="date", y="sales", label="Sales")
sns.lineplot(data=df, x="date", y="temperature", label="Temperature")

plt.title("Multi-variable Time Series")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare patterns between variables

# --------------------------------------------
