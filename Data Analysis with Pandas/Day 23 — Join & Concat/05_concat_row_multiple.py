# =========================================
# Multiple Rows Concat
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")

# 👉 same dataset multiple times
df = pd.concat([emp, emp, emp], axis=0)

print(df)

# 👉 explanation:
# data stacking (data augmentation style)