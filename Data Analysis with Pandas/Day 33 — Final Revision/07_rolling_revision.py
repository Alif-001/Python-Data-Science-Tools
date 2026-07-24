# =========================================
# ROLLING REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# 👉 moving average
df['Rolling'] = df['Salary'].rolling(window=2).mean()

print(df)

# 👉 revision:
# rolling = trend smoothing