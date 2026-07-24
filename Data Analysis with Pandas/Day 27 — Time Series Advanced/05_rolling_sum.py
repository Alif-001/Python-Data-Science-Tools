# =========================================
# rolling() with sum
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 3-day rolling total sales
df['Rolling_Sum'] = df['Sales'].rolling(window=3).sum()

print(df)

# 👉 explanation:
# moving total sales trend