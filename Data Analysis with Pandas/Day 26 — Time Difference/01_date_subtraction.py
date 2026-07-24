# =========================================
# Date Subtraction (Time Difference)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 string → datetime convert
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['LeaveDate'] = pd.to_datetime(df['LeaveDate'])

# 👉 time difference বের করা
df['Work_Duration'] = df['LeaveDate'] - df['JoinDate']

print(df)

# 👉 explanation:
# LeaveDate - JoinDate = কতদিন কাজ করেছে