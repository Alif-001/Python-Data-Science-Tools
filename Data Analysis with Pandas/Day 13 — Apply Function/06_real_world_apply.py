# =========================================
# Real-world Apply Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 salary tax calculate (10%)
df['Tax'] = df['Salary'].apply(lambda x: x * 0.10)

# 👉 net salary
df['Net_Salary'] = df['Salary'] - df['Tax']

# 👉 performance label
df['Performance'] = df['Marks'].apply(
    lambda x: "Excellent" if x >= 90 else ("Good" if x >= 80 else "Average")
)

print(df)

# 👉 summary:
# apply = custom logic apply tool