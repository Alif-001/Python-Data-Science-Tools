# =========================================
# Extract Month
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 month বের করা
df['Month'] = df['JoinDate'].dt.month

print(df)

# 👉 explanation:
# dt.month → month number (1-12)