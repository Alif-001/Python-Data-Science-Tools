# =========================================
# Multiple Dataset Concat
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

# 👉 merge all horizontally
df = pd.concat([emp, sal, bonus], axis=1)

print(df)

# 👉 explanation:
# multiple datasets combine করা যায়