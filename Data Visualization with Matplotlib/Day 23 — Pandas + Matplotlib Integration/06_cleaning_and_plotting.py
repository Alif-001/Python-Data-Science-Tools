import pandas as pd
import matplotlib.pyplot as plt

"""
DATA CLEANING + PLOTTING
-----------------------
Real datasets often need preprocessing.
"""

df = pd.read_csv("sales_data_dirty.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Handle missing values (fill with previous value)
df["sales"] = df["sales"].fillna(method="ffill")

df.plot(x="date", y="sales", marker="o")

plt.title("Cleaned Data Plot")
plt.xticks(rotation=45)

plt.show()