# =========================================
# to_datetime() - Date Conversion
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 JoinDate string → datetime convert
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)

# 👉 এখন আমরা date থেকে part বের করতে পারি

print(df['JoinDate'].dt.year)
print(df['JoinDate'].dt.month)
print(df['JoinDate'].dt.day)

# 👉 explanation:
# datetime = time-based analysis এর জন্য দরকার