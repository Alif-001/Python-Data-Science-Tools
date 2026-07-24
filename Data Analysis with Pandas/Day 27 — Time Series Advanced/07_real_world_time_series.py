# =========================================
# Real-world Time Series Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 daily trend
df['Rolling_3day'] = df['Sales'].rolling(window=3).mean()

# 👉 weekly trend
weekly = df.resample('W').sum()

# 👉 insight
print("Daily Data with Trend:\n", df)
print("\nWeekly Summary:\n", weekly)

print("\nBest Sales Day:")
print(df['Sales'].idxmax())

# 👉 explanation:
# time series = forecasting + business analytics core