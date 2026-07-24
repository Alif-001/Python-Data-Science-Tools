# =========================================
# Resample + Rolling Together
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 Step 1: weekly sales
weekly = df.resample('W').sum()

# 👉 Step 2: rolling average (smooth trend)
weekly['Rolling_Avg'] = weekly['Sales'].rolling(window=2).mean()

print(weekly)

# 👉 explanation:
# resample = scale change
# rolling = trend smoothing