# =========================================
# Project-style Time Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['LeaveDate'] = pd.to_datetime(df['LeaveDate'])

# 👉 Step 1: duration
df['Days_Worked'] = (df['LeaveDate'] - df['JoinDate']).dt.days

# 👉 Step 2: category
df['Experience_Level'] = df['Days_Worked'].apply(
    lambda x: "Senior" if x > 700 else ("Mid" if x > 300 else "Junior")
)

# 👉 Step 3: summary
avg_days = df['Days_Worked'].mean()

print(df)
print("\nAverage Working Days:", avg_days)

# 👉 explanation:
# time difference → business insight + HR analytics