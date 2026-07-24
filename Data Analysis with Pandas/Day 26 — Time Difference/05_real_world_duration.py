# =========================================
# Real-world Time Difference Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['LeaveDate'] = pd.to_datetime(df['LeaveDate'])

# 👉 duration in days
df['Days_Worked'] = (df['LeaveDate'] - df['JoinDate']).dt.days

# 👉 monthly estimate
df['Months_Worked'] = df['Days_Worked'] / 30

print(df)

# 👉 insight
print("\nLongest working employee:")
print(df.loc[df['Days_Worked'].idxmax()])

# 👉 explanation:
# HR analytics = time tracking system