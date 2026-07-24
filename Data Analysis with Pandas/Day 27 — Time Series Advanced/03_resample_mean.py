# =========================================
# resample() with mean
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 weekly average sales
weekly_avg = df.resample('W').mean()

print(weekly_avg)

# 👉 explanation:
# average trend analysis