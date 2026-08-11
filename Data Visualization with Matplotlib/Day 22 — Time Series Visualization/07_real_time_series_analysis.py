import matplotlib.pyplot as plt
import pandas as pd

"""
REAL TIME SERIES ANALYSIS
-------------------------
We use real CSV data and plot trends.
"""

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Plot
plt.plot(df["date"], df["sales"], marker="o")

plt.title("Real Sales Time Series")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()