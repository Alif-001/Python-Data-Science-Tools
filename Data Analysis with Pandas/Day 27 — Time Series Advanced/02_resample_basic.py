# =========================================
# resample() - Time Grouping
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 weekly sales (W = week)
weekly_sales = df.resample('W').sum()

print(weekly_sales)

# 👉 explanation:
# daily → weekly data convert করা