# =========================================
# Convert to Time Series Index
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Date কে datetime বানানো
df['Date'] = pd.to_datetime(df['Date'])

# 👉 Date কে index বানানো (time series জন্য important)
df = df.set_index('Date')

print(df)

# 👉 explanation:
# time series analysis এর জন্য date index দরকার