# =========================================
# Column-wise apply
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple column এ apply

# 👉 numeric columns average বের করা
result = df[['Age', 'Salary', 'Marks']].apply(lambda x: x.mean())

print(result)

# 👉 explanation:
# default axis = 0 (column-wise)
# প্রতিটি column এ function apply হয়