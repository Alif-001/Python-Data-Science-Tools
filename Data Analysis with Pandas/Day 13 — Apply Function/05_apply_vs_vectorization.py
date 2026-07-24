# =========================================
# apply() vs direct operation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 apply দিয়ে
df['Double_Salary_apply'] = df['Salary'].apply(lambda x: x * 2)

# 👉 direct vectorized operation (recommended)
df['Double_Salary_direct'] = df['Salary'] * 2

print(df)

# 👉 explanation:
# vectorized operation faster than apply
# real-world: direct operation prefer করা উচিত