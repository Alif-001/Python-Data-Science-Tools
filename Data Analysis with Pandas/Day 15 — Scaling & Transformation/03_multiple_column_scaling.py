# =========================================
# Scaling Multiple Columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Age scaling
df['Age_scaled'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

# 👉 Marks scaling
df['Marks_scaled'] = (df['Marks'] - df['Marks'].min()) / (df['Marks'].max() - df['Marks'].min())

print(df)

# 👉 explanation:
# multiple feature scaling → better ML performance