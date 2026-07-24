# =========================================
# to_numeric() - Safe Numeric Conversion
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 safer way to convert numeric
df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

print(df.dtypes)

# 👉 advantage:
# errors থাকলে handle করা যায়

# 👉 example (error ignore)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')