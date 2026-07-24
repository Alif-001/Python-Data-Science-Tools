# =========================================
# concat - Column-wise (axis=1)
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 column wise combine
df = pd.concat([emp, sal], axis=1)

print(df)

# 👉 explanation:
# axis=1 → পাশাপাশী যুক্ত হয়