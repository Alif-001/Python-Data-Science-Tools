# =========================================
# rolling() - Moving Window
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 3-day moving average
df['Rolling_Mean'] = df['Sales'].rolling(window=3).mean()

print(df)

# 👉 explanation:
# rolling = smooth trend (noise reduce)