# =========================================
# Multiple Column Statistics
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 একসাথে multiple column stats
print(df[['Age', 'Salary', 'Marks']].mean())

print(df[['Age', 'Salary', 'Marks']].sum())

# 👉 explanation:
# multiple column select করে stats apply করা যায়