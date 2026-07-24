# =========================================
# expanding() - Cumulative Window
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 👉 expanding mean (start থেকে এখন পর্যন্ত)
df['Expanding_Mean'] = df['Sales'].expanding().mean()

print(df)

# 👉 explanation:
# যত data বাড়ে, তত full history consider করে