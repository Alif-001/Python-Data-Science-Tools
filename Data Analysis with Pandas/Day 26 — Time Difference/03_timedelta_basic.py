# =========================================
# timedelta - Add/Subtract Time
# =========================================

import pandas as pd
from datetime import timedelta

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 30 দিন add করা
df['After_30_Days'] = df['JoinDate'] + timedelta(days=30)

# 👉 10 দিন subtract করা
df['Before_10_Days'] = df['JoinDate'] - timedelta(days=10)

print(df)

# 👉 explanation:
# timedelta = time add/subtract tool