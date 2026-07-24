# =========================================
# filter() - Filter groups
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 শুধু সেই department রাখবো যাদের average salary > 30000

filtered = df.groupby('Department').filter(
    lambda x: x['Salary'].mean() > 30000
)

print(filtered)

# 👉 explanation:
# group level condition apply হয়