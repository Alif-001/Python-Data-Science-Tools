# =========================================
# Real-world Advanced GroupBy Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Department + City wise analysis
group = df.groupby(['Department', 'City'])

# 👉 multiple stats
result = group['Salary'].agg(['mean', 'max', 'min'])

print(result)

# 👉 insight
print("\nHighest paying group:")
print(result['mean'].idxmax())

# 👉 explanation:
# multi-level analysis = business insights