# =========================================
# Time Series Setup
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Date কে datetime বানানো
df['Date'] = pd.to_datetime(df['Date'])

# 👉 Date কে index করা (time series এর জন্য দরকার)
df = df.set_index('Date')

print(df)

# 👉 explanation:
# window function কাজ করার জন্য time index দরকার