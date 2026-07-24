# =========================================
# Custom Time Calculation
# =========================================

import pandas as pd
from datetime import timedelta

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 1 year (365 days) add
df['After_1_Year'] = df['JoinDate'] + timedelta(days=365)

# 👉 6 months approx (180 days)
df['After_6_Months'] = df['JoinDate'] + timedelta(days=180)

print(df)

# 👉 explanation:
# business analysis + prediction style calculation