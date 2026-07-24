# =========================================
# expanding() - Cumulative Sum
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 total cumulative sales
df['Cumulative_Sales'] = df['Sales'].expanding().sum()

print(df)

# 👉 explanation:
# শুরু থেকে এখন পর্যন্ত total sum