# =========================================
# All Date Features Together
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 multiple extraction
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month
df['Day'] = df['JoinDate'].dt.day

print(df)

# 👉 explanation:
# একসাথে time breakdown করা যায়