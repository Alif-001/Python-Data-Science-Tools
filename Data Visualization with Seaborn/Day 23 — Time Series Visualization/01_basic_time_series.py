# 01_basic_time_series.py

# --------------------------------------------

# DAY 23: TIME SERIES VISUALIZATION

# --------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv("sales_data.csv")

# Convert date column to datetime format

df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------

# BASIC TIME SERIES LINE PLOT

# --------------------------------------------

sns.lineplot(
data=df,
x="date",
y="sales"
)

plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------

# IDEA:

# - x-axis = time

# - y-axis = value trend

# --------------------------------------------
