# =========================================
# Real-world Window Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 short term trend
df['Rolling_3'] = df['Sales'].rolling(window=3).mean()

# 👉 long term trend
df['Expanding'] = df['Sales'].expanding().mean()

print(df)

# 👉 insight
print("\nMax Sales Day:")
print(df['Sales'].idxmax())

# 👉 explanation:
# rolling = short-term trend
# expanding = long-term trend