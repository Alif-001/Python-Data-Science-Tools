# =========================================
# Extract Day
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 day বের করা
df['Day'] = df['JoinDate'].dt.day

print(df)

# 👉 explanation:
# dt.day → date (1-31)