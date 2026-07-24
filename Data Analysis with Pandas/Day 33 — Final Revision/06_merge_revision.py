# =========================================
# MERGE REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

# 👉 split salary dataset (simulation)
salary = df[['EmpID', 'Salary']]

# 👉 merge (self example)
merged = pd.merge(df, salary, on='EmpID', how='left')

print(merged)

# 👉 revision:
# merge = dataset join