# =========================================
# rolling() - Moving Window
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 3-day rolling average
df['Rolling_Mean'] = df['Sales'].rolling(window=3).mean()

print(df)

# 👉 explanation:
# প্রতিবার 3 দিন নিয়ে average হিসাব করে