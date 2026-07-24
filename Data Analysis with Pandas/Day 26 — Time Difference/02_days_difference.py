# =========================================
# Convert Time Difference to Days
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['LeaveDate'] = pd.to_datetime(df['LeaveDate'])

# 👉 difference
df['Work_Duration'] = df['LeaveDate'] - df['JoinDate']

# 👉 days হিসেবে convert
df['Days_Worked'] = df['Work_Duration'].dt.days

print(df)

# 👉 explanation:
# .dt.days → number of days বের করে