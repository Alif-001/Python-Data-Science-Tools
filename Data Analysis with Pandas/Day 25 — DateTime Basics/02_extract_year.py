# =========================================
# Extract Year
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 year বের করা
df['Year'] = df['JoinDate'].dt.year

print(df)

# 👉 explanation:
# dt.year → শুধু year part বের করে