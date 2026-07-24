# =========================================
# concat - Row-wise (axis=0)
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")

# 👉 same structure dataset duplicate করার মতো
df = pd.concat([emp, emp], axis=0)

print(df)

# 👉 explanation:
# axis=0 → নিচে নিচে যুক্ত হয়