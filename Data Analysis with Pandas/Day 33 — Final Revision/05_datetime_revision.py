# =========================================
# DATETIME REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

# 👉 convert to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 extract features
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month

print(df)

# 👉 revision:
# time → feature extraction